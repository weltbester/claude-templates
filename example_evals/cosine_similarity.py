#!/usr/bin/env python3
"""
FAQ Consistency Evaluator
=========================
This program tests whether an AI assistant (Claude) gives consistent answers
to the same customer service question even when that question is phrased
differently — with typos, unnecessary detail, or irrelevant background info.

HOW IT WORKS (plain English):
  1. We prepare groups of questions. Each group asks the same thing in
     different ways (e.g. "What is your return policy?" vs. a version full
     of typos).
  2. We send every question to Claude and collect its answers.
  3. We convert those answers into lists of numbers (called "embeddings")
     that capture their meaning. Answers that mean the same thing will
     produce similar sets of numbers.
  4. We measure how similar those number-lists are to each other using a
     method called cosine similarity (see below).
  5. We print a score for each question group. A score close to 100% means
     Claude answered consistently regardless of how the question was worded.
     A low score means the different phrasings led to meaningfully different
     answers.

WHAT IS COSINE SIMILARITY? (plain English):
  Imagine each answer is represented as an arrow pointing in some direction
  in space. Two answers that mean the same thing point in nearly the same
  direction; the angle between them is small. Cosine similarity measures
  how closely two arrows point together: 100% means identical direction
  (same meaning), 0% means perpendicular (completely unrelated meaning).

  Important: we only compare *different* answers to each other. Comparing
  an answer to itself would always give 100% and make the score misleadingly
  high — so we exclude those self-comparisons (the "diagonal" of the
  comparison table).
"""

import anthropic
import numpy as np
from sentence_transformers import SentenceTransformer


# ---------------------------------------------------------------------------
# TEST DATA
# Each entry below is one "FAQ group": a set of questions that all ask the
# same thing, but in a different style. The "answer" field holds the ideal
# response (not currently used in scoring, but useful for future expansion).
# ---------------------------------------------------------------------------

faq_variations = [
    {
        # Edge case: typos — does Claude understand garbled input?
        "questions": [
            "What is your return policy?",
            "How can I return an item?",
            "Wut's yur retrn polcy?",
        ],
        "answer": "Our return policy allows..."
    },
    {
        # Edge case: long, rambling questions — does Claude stay on topic
        # when buried under unnecessary detail?
        "questions": [
            "I bought something last week, and it's not really what I expected, so I was wondering if maybe I could possibly return it?",
            "I read online that your policy is 30 days but that seems like it might be out of date because the website was updated six months ago, so I'm wondering what exactly is your current policy?",
        ],
        "answer": "Our return policy allows..."
    },
    {
        # Edge case: irrelevant information — does Claude ignore distracting
        # context and still answer the real question?
        "questions": [
            "I'm Jane's cousin, and she said you guys have great customer service. Can I return this?",
            "Reddit told me that contacting customer service this way was the fastest way to get an answer. I hope they're right! What is the return window for a jacket?",
        ],
        "answer": "Our return policy allows..."
    },
]


# ---------------------------------------------------------------------------
# Set up the Anthropic client. It reads your API key automatically from the
# ANTHROPIC_API_KEY environment variable.
# ---------------------------------------------------------------------------
client = anthropic.Anthropic()


def get_completion(prompt: str) -> str:
    """
    Send a single question to Claude and return its text answer.

    Parameters
    ----------
    prompt : the question to ask Claude

    Returns
    -------
    Claude's answer as a plain string
    """
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def evaluate_cosine_similarity(outputs: list[str]) -> float:
    """
    Measure how semantically consistent a list of answers are with each other.

    Steps
    -----
    1. Convert each answer into an "embedding" — a list of ~384 numbers that
       encodes the meaning of the text. This is done by a small, fast AI model
       called all-MiniLM-L6-v2 that runs locally on your machine.

    2. Build a comparison table (matrix) where every answer is compared to
       every other answer using cosine similarity.

    3. Discard the diagonal of that table — those are each answer compared to
       itself, which always scores 1.0 (100%) and would inflate the result.

    4. Return the average of all remaining (answer-vs-different-answer) scores.

    Parameters
    ----------
    outputs : list of answer strings to compare

    Returns
    -------
    A float between 0.0 and 1.0. Multiply by 100 to get a percentage.
    """
    # Load the local embedding model (downloaded once, then cached on disk).
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Turn each answer string into a fixed-size list of numbers (an embedding).
    embeddings = model.encode(outputs)

    # Compute the "length" of each embedding vector so we can normalise later.
    norms = np.linalg.norm(embeddings, axis=1)

    # Build the full pairwise cosine-similarity table:
    #   - np.dot(embeddings, embeddings.T) gives the dot product of every pair
    #   - dividing by np.outer(norms, norms) normalises each value to [-1, 1]
    cosine_similarities = np.dot(embeddings, embeddings.T) / np.outer(norms, norms)

    # Remove the diagonal (self-comparisons that always equal 1.0).
    # Replacing them with NaN lets us use nanmean, which ignores NaN values,
    # so the average is computed only over genuine cross-answer comparisons.
    np.fill_diagonal(cosine_similarities, np.nan)

    return np.nanmean(cosine_similarities)


def main() -> None:
    """
    Run the evaluation over every FAQ group and print a consistency score.

    For each group:
      - Ask Claude every question variant and collect the answers.
      - Score how similar those answers are to each other.
      - Print the score. Higher is better (more consistent).
    """
    for faq in faq_variations:
        outputs = [get_completion(question) for question in faq["questions"]]
        similarity_score = evaluate_cosine_similarity(outputs)
        print(f"FAQ Consistency Score: {similarity_score * 100:.2f}%")


if __name__ == "__main__":
    main()
