import random

human_responses = [
    "Haha that's interesting!",
    "I think it depends on the situation.",
    "That reminds me of something I read.",
    "I'm not completely sure about that.",
    "Hmm, let me think about it."
]

machine_responses = [
    "Processing input using internal logic.",
    "Query received. Generating response.",
    "Executing predefined response pattern.",
    "Analyzing question structure.",
    "Optimal output computed."
]


def judge(response):
    suspicious_words = [
        "processing", "executing", "optimal",
        "analyzing", "query", "computed"
    ]

    score = 0
    text = response.lower()

    for word in suspicious_words:
        if word in text:
            score += 20

    if score >= 40:
        return "BOT"
    else:
        return "HUMAN"


def main():
    print("=== TURING TEST SIMULATION ===")
    question = input("Judge: ")

    human_reply = random.choice(human_responses)
    machine_reply = random.choice(machine_responses)

    print("\nHuman says:", human_reply)
    print("Machine says:", machine_reply)

    print("\nJudge Verdict:")
    print("Human ->", judge(human_reply))
    print("Machine ->", judge(machine_reply))


if __name__ == "__main__":
    main()
