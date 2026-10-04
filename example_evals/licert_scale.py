#!/usr/bin/python3
"""
Likert-Scale Tone Evaluation for AI Customer Service Responses
==============================================================
What this script does (for non-programmers)
--------------------------------------------
This script measures how well Claude responds to customer inquiries in the
correct tone (e.g. empathetic, patient, professional).

It works in three steps:
  1. For each customer message, ask Claude to write a customer service reply.
  2. Ask Claude to rate its own reply on a 1-to-5 scale for the required tone.
  3. Print the average tone score across all inquiries.

What is a Likert scale?
------------------------
A Likert scale is a numbered rating system — here 1 to 5 — used to measure
how strongly something matches a quality:
  1 = Not at all [tone]
  5 = Perfectly [tone]
It is widely used in surveys and AI evaluations because it captures degrees
of quality rather than a simple yes/no.

Why does Claude evaluate its own output?
-----------------------------------------
The script uses Claude both to generate the reply AND to score it. This is a
common pattern in AI evaluation called "LLM-as-judge". A second AI call acts
as an automated quality checker, removing the need for a human to read every
single response. Note that using the same model to judge itself can introduce
bias; using a separate, independent model is generally more reliable.

How to read the output
-----------------------
The script prints one line, e.g.:
  Average Tone Score: 3.8
Scores range from 1 (poor tone match) to 5 (perfect tone match). A score
above 4 is generally considered good for customer service applications.

Library Assessment
------------------
  anthropic (current):
    The only import. Actively maintained by Anthropic and suitable for
    production use. No replacement needed.
"""

import anthropic

# Each inquiry pairs a customer message with the tone Claude's reply must match.
# Edge cases are included to test whether Claude handles emotionally charged or
# ambiguous messages without defaulting to a generic, off-tone response.
inquiries = [
    {
        "text": "This is the third time you've messed up my order. I want a refund NOW!",
        "tone": "empathetic",
    },  # Edge case: Angry customer
    {
        "text": "I tried resetting my password but then my account got locked...",
        "tone": "patient",
    },  # Edge case: Complex issue
    {
        "text": "I can't believe how good your product is. It's ruined all others for me!",
        "tone": "professional",
    },  # Edge case: Compliment as complaint
    # ... 97 more inquiries
]

client = anthropic.Anthropic()


def get_completion(prompt: str):
    message = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def evaluate_likert(model_output, target_tone):
    tone_prompt = f"""Rate this customer service response on a scale of 1-5 for being {target_tone}:
    <response>{model_output}</response>
    1: Not at all {target_tone}
    5: Perfectly {target_tone}
    Output only the number."""

    # Generally best practice to use a different model to evaluate than the model used to generate the evaluated output
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=50,
        messages=[{"role": "user", "content": tone_prompt}],
    )
    # strip() removes any leading/trailing whitespace or newlines the model may
    # add; without it, int() would raise a ValueError on " 4\n" for example.
    return int(response.content[0].text.strip())


# Step 1: Generate a customer service reply for every inquiry.
outputs = [
    get_completion(f"Respond to this customer inquiry: {inquiry['text']}")
    for inquiry in inquiries
]

# Step 2: Score each reply for the required tone.
# zip() keeps outputs[i] paired with inquiries[i] so scores match the right reply.
tone_scores = [
    evaluate_likert(output, inquiry["tone"])
    for output, inquiry in zip(outputs, inquiries)
]

# Step 3: Report the mean Likert score across all inquiries.
print(f"Average Tone Score: {sum(tone_scores) / len(tone_scores)}")
