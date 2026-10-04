#!/usr/bin/env python3
"""
ROUGE-L Evaluation for AI-Generated Article Summaries
======================================================
What this script does (for non-programmers)
--------------------------------------------
This script tests how well Claude (an AI model) summarizes news articles
compared to human-written reference summaries.

It works in three steps:
  1. Feed each article to Claude and ask it to produce a 1-2 sentence summary.
  2. Compare Claude's summary to a pre-written "gold standard" summary using a
     metric called ROUGE-L (explained below).
  3. Print the average ROUGE-L score across all articles so you can judge
     overall summary quality.

What is ROUGE-L?
----------------
ROUGE-L measures how much wording two summaries share by finding the longest
sequence of words that appear in the same order in both texts.
The result is an F1 score between 0 and 1:
  - 1.0  = perfect match (Claude's summary and the reference are identical)
  - 0.0  = no overlap at all
  - ~0.4-0.6 is considered good for summarization tasks

Why use ROUGE-L instead of exact matching?
------------------------------------------
Human language is flexible — two sentences can mean the same thing with
different words. ROUGE-L rewards partial overlap, giving credit for shared
phrases even when the wording isn't identical.

How to read the output
-----------------------
The script prints one line, e.g.:
  Average ROUGE-L F1 Score: 0.47
A higher number means Claude's summaries are closer to the human references.

Library Recommendation
-----------------------
  rouge (current):
    Unmaintained — last released in 2018. Not suitable for paying customers
    due to the security and support liability of an abandoned dependency.

  anthropic (current):
    Actively maintained. Fine for production use.

  Recommended replacement for rouge:
    `rouge-score` (pip install rouge-score) — Google's actively maintained
    implementation, or `evaluate` (pip install evaluate) from Hugging Face
    for a broader NLP metrics library that includes ROUGE-L.

Production Readiness Assessment
---------------------------------
Beyond the library issue above, the following code-level gaps should be
addressed before using this script in a pipeline or CI workflow:

  GAP 1 — No fault tolerance
    Any network hiccup, API timeout, or rate-limit response will crash the
    entire run. With 200 articles this is practically guaranteed to happen.
    Recommended tool: `tenacity` (pip install tenacity)
      Wraps get_completion() with automatic exponential-backoff retries.
      Example: @retry(wait=wait_exponential(min=1, max=60), stop=stop_after_attempt(5))

  GAP 2 — No result persistence / checkpointing
    Only the final average is printed. If the script fails at article 190,
    all prior API calls and scores are lost.
    Recommended tool: stdlib `json` or `csv`
      Write each (article_id, model_output, rouge_l_score) to a file after
      every article so a restart can skip already-processed entries.

  GAP 3 — No progress visibility
    200 silent API calls give no indication of how long remains.
    Recommended tool: `tqdm` (pip install tqdm)
      Wrap the list comprehensions in tqdm() to get a live progress bar.

  GAP 4 — Sequential execution is slow
    Each API call blocks until the previous one returns. The Anthropic SDK
    ships an async client that supports concurrent requests.
    Recommended tool: stdlib `asyncio` + `anthropic.AsyncAnthropic`
      Run multiple summarization requests in parallel to cut wall-clock time
      significantly (e.g., asyncio.gather() over all articles).

  GAP 5 — Hardcoded configuration
    Model name ("claude-opus-4-8") and max_tokens (1024) are baked into the
    code, making model-comparison experiments require source edits.
    Recommended tool: stdlib `argparse` or `python-dotenv` (pip install python-dotenv)
      Expose model, max_tokens, and dataset path as CLI flags or env vars.

  GAP 6 — No structured logging
    A bare print() is invisible in CI logs and carries no severity level,
    timestamp, or article-level detail.
    Recommended tool: stdlib `logging`
      Replace print() with logging.info() / logging.warning() and configure
      a formatter with timestamps and log levels.

Summary of recommended additions
  pip install tenacity tqdm python-dotenv
  Use stdlib: json (or csv), argparse, logging, asyncio
"""

# rouge is unmaintained (last release 2018); replace with rouge-score or evaluate
from rouge import Rouge
import anthropic

# Each entry pairs the raw article text with a human-written "gold standard"
# summary. The edge-case articles (multi-topic, misleading title) stress-test
# whether Claude handles tricky real-world inputs gracefully.
articles = [
    {
        "text": "In a groundbreaking study, researchers at MIT...",
        "summary": "MIT scientists discover a new antibiotic...",
    },
    {
        "text": "Jane Doe, a local hero, made headlines last week for saving... In city hall news, the budget... Meteorologists predict...",
        "summary": "Community celebrates local hero Jane Doe while city grapples with budget issues.",
    },  # Edge case: Multi-topic
    {
        "text": "You won't believe what this celebrity did! ... extensive charity work ...",
        "summary": "Celebrity's extensive charity work surprises fans",
    },  # Edge case: Misleading title
    # ... 197 more articles
]

client = anthropic.Anthropic()


def get_completion(prompt: str):
    message = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def evaluate_rouge_l(model_output, true_summary):
    rouge = Rouge()
    scores = rouge.get_scores(model_output, true_summary)
    # get_scores returns a list of dicts; [0] picks the first (and only) pair.
    # "f" is the F1 score — the balanced average of precision and recall.
    return scores[0]["rouge-l"]["f"]


# Step 1: Ask Claude to summarize each article (one API call per article).
outputs = [
    get_completion(f"Summarize this article in 1-2 sentences:\n\n{article['text']}")
    for article in articles
]

# Step 2: Score each Claude summary against the matching gold standard.
# zip() pairs outputs[i] with articles[i] so the order stays in sync.
relevance_scores = [
    evaluate_rouge_l(output, article["summary"])
    for output, article in zip(outputs, articles)
]

# Step 3: Report the mean score across the whole dataset.
print(f"Average ROUGE-L F1 Score: {sum(relevance_scores) / len(relevance_scores)}")
