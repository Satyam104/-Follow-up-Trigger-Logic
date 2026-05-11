CORRECTNESS_LIMIT  = 0.6
DEPTH_LIMIT        = 0.5
COMPLETENESS_LIMIT = 0.7
MAX_ATTEMPTS       = 3


def is_answer_empty(answer):
    if answer is None:
        return True
    if answer.strip() == "":
        return True
    return False


def is_correctness_low(score):
    return score < CORRECTNESS_LIMIT

def is_depth_low(score):
    return score < DEPTH_LIMIT

def is_completeness_low(score):
    return score < COMPLETENESS_LIMIT


def too_many_attempts(attempts):
    return attempts >= MAX_ATTEMPTS


def check_followup(answer, correctness, depth, completeness, attempts):

    if too_many_attempts(attempts):
        return {
            "follow_up_needed": False,
            "type": None,
            "reason": "Asked too many times already. Moving on."
        }

    if is_answer_empty(answer):
        return {
            "follow_up_needed": True,
            "type": "clarification",
            "reason": "The answer is empty. Please provide a response."
        }

    if is_correctness_low(correctness):
        return {
            "follow_up_needed": True,
            "type": "correction",
            "reason": "The answer has errors. Please correct it."
        }

    if is_completeness_low(completeness):
        return {
            "follow_up_needed": True,
            "type": "clarification",
            "reason": "Some information is missing. Please add more details."
        }

    if is_depth_low(depth):
        return {
            "follow_up_needed": True,
            "type": "deep_dive",
            "reason": "The answer needs more depth. Please explain further."
        }

    return {
        "follow_up_needed": False,
        "type": None,
        "reason": "Answer quality is good. No follow-up needed."
    }


def show_result(result):
    print(f"  Follow-up Needed : {result['follow_up_needed']}")
    print(f"  Type             : {result['type']}")
    print(f"  Reason           : {result['reason']}")


def run_all_tests():

    tests = [
        {
            "label": "Empty Answer",
            "answer": "", "correctness": 0.9,
            "depth": 0.9, "completeness": 0.9, "attempts": 0
        },
        {
            "label": "Wrong Answer",
            "answer": "Python is a type of snake only",
            "correctness": 0.2, "depth": 0.8,
            "completeness": 0.9, "attempts": 0
        },
        {
            "label": "Shallow Answer",
            "answer": "FastAPI is fast.",
            "correctness": 0.9, "depth": 0.3,
            "completeness": 0.8, "attempts": 0
        },
        {
            "label": "Incomplete Answer",
            "answer": "You can use a database.",
            "correctness": 0.8, "depth": 0.7,
            "completeness": 0.4, "attempts": 0
        },
        {
            "label": "Good Answer",
            "answer": "Python is a high-level programming language used for web, AI, and data science.",
            "correctness": 0.9, "depth": 0.8,
            "completeness": 0.9, "attempts": 0
        },
        {
            "label": "Too Many Attempts",
            "answer": "Bad answer",
            "correctness": 0.1, "depth": 0.1,
            "completeness": 0.1, "attempts": 3
        },
    ]

    print("\n" + "=" * 45)
    print("      FOLLOW-UP CHECKER — TEST RESULTS")
    print("=" * 45)

    for i, t in enumerate(tests, start=1):
        result = check_followup(
            t["answer"], t["correctness"],
            t["depth"], t["completeness"], t["attempts"]
        )
        print(f"\n[TEST {i}] {t['label']}")
        print("-" * 45)
        show_result(result)

    print("\n" + "=" * 45)


def interactive_mode():

    print("\n" + "=" * 45)
    print("      INTERACTIVE MODE")
    print("=" * 45)

    answer       = input("\nEnter the AI answer        : ")
    correctness  = float(input("Correctness score (0 - 1)  : "))
    depth        = float(input("Depth score (0 - 1)        : "))
    completeness = float(input("Completeness score (0 - 1) : "))
    attempts     = int(input("Follow-ups asked so far    : "))

    result = check_followup(answer, correctness, depth, completeness, attempts)

    print("\n" + "-" * 45)
    show_result(result)
    print("-" * 45)


if __name__ == "__main__":

    print("\n" + "=" * 45)
    print("      FOLLOW-UP QUESTION CHECKER")
    print("=" * 45)

    run_all_tests()

    choice = input("\nTry with your own values? (yes / no) : ")
    if choice.strip().lower() == "yes":
        interactive_mode()

    print("\nProgram finished. Goodbye!\n")
