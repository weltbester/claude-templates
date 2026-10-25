#!/usr/bin/env python3

import anthropic

tweets = [
    {"text": "This movie was a total waste of time. 👎", "sentiment": "negative"},
    {"text": "The new album is 🔥! Been on repeat all day.", "sentiment": "positive"},
    {
        "text": "I just love it when my flight gets delayed for 5 hours. #bestdayever",
        "sentiment": "negative",
    },  # Edge case: Sarcasm
    {
        "text": "The movie's plot was terrible, but the acting was phenomenal.",
        "sentiment": "mixed",
    },  # Edge case: Mixed sentiment 
]

client = anthropic.Anthropic()

def get_completion(prompt: str):
    message = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=50,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text

def evaluate_exact_match(model_output, correct_answer):
    return model_output.strip().lower() == correct_answer.lower()

outputs = [
    get_completion(
        f"Classify this only with the words 'positive', 'negative' 'neutral' or 'mixed': {tweet['text']}"
    )
    for tweet in tweets
]

print(outputs)

def main():
    accuracy = sum(
        evaluate_exact_match(output, tweet["sentiment"])
        for output, tweet in zip(outputs, tweets)
    ) / len(tweets)

    print(f"Sentiment Analysis Accuray: {accuracy * 100}%")

if __name__ == "__main__":
        main()
