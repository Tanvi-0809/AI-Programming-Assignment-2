"""
CAPTCHA System (Toy Implementation)
Author: Tanvi Gajula
Roll No: SE24UCSE025
Course: Artificial Intelligence
"""

import random
import string


def generate_session_id(n=10):
    return "".join(random.choice("0123456789ABCDEF") for _ in range(n))


def captcha_math():
    a = random.randint(5, 30)
    b = random.randint(5, 30)
    return f"What is {a} + {b}?", str(a + b)


def captcha_logic():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    d = random.choice(days[:-1])
    return f"What comes after {d}?", days[days.index(d) + 1]


def captcha_text():
    code = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    return f"Enter this code: {code}", code


def main():
    print("=== CAPTCHA SYSTEM ===")
    print("Session ID:", generate_session_id())

    kind = random.choice(["math", "logic", "text"])
    if kind == "math":
        question, correct = captcha_math()
    elif kind == "logic":
        question, correct = captcha_logic()
    else:
        question, correct = captcha_text()

    print("Challenge:", question)
    user = input("Response: ").strip()

    if user.lower() == correct.lower():
        print("Result: Access Granted ✅")
    else:
        print("Result: Access Blocked ❌")


if __name__ == "__main__":
    main()
