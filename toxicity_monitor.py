import sys

TOXIC_WORDS = {
    "insult": ["stupid", "idiot", "dumb", "loser"],
    "hate": ["hate", "kill", "disgusting"],
    "aggression": ["shut up", "i'll hit you", "fight"],
}

def analyze_text(text):
    text_lower = text.lower()
    flags = []
    score = 0

    for category, words in TOXIC_WORDS.items():
        for w in words:
            if w in text_lower:
                flags.append(category)
                score += 30

    score = min(score, 100)
    return score, list(set(flags))

def analyze_file(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            score, flags = analyze_text(line)
            print(f'Text: "{line}"')
            print(f"Toxicity: {score}%")
            print(f"Flags: {', '.join(flags) if flags else 'none'}")
            print("-" * 40)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python toxicity_monitor.py <text or file>")
        sys.exit(1)

    arg = sys.argv[1]

    # detect if argument is a file
    if arg.endswith(".txt"):
        analyze_file(arg)
    else:
        text = " ".join(sys.argv[1:])
        score, flags = analyze_text(text)
        print(f'Text: "{text}"')
        print(f"Toxicity: {score}%")
        print(f"Flags: {", ".join(flags) if flags else "none"}')
