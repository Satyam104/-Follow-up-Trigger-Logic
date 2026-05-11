# -Follow-up-Trigger-Logic
# 🤖 Follow-up Trigger Logic

---

## 💡 What Does This Project Do?

When an AI gives an answer, this program checks:

- Is the answer **empty**?
- Is the answer **incorrect**?
- Is the answer **incomplete**?
- Is the answer **too shallow**?

Based on these checks, it decides whether to ask a follow-up question or accept the answer.

---

## 📁 Project Structure

```
followup-trigger-logic/
│
├── followup_trigger_logic.py     ← main program file
└── README.md               ← this file
```

---

## ⚙️ How It Works

The program checks the answer quality using three scores (all between 0.0 and 1.0):

| Score | What It Means | Minimum Required |
|---|---|---|
| `correctness` | How accurate the answer is | 0.6 |
| `depth` | How detailed the answer is | 0.5 |
| `completeness` | How complete the answer is | 0.7 |

If any score is below the limit → a follow-up is triggered.

### Follow-up Types

| Problem Detected | Follow-up Type |
|---|---|
| Answer is empty | `clarification` |
| Answer is wrong | `correction` |
| Answer is incomplete | `clarification` |
| Answer is too shallow | `deep_dive` |
| Too many attempts (3+) | No follow-up (stops) |

---

## 🖥️ Sample Output

```
=============================================
      FOLLOW-UP TRIGGER LOGIC — TEST RESULTS
=============================================

[TEST 1] Empty Answer
---------------------------------------------
  Follow-up Needed : True
  Type             : clarification
  Reason           : The answer is empty. Please provide a response.

[TEST 2] Wrong Answer
---------------------------------------------
  Follow-up Needed : True
  Type             : correction
  Reason           : The answer has errors. Please correct it.

[TEST 5] Good Answer
---------------------------------------------
  Follow-up Needed : False
  Type             : None
  Reason           : Answer quality is good. No follow-up needed.
```

---

## 🚀 How to Run

**Requirements:** Python 3.7 or above. No extra libraries needed.

**Step 1 — Clone the repository**

```bash
git clone https://github.com/your-username/followup-trigger-logic.git
cd followup-trigger-logic
```

**Step 2 — Run the program**

```bash
python followup_trigger_logic.py
```

**Step 3 — Try interactive mode**

After the test cases finish, the program will ask:

```
Try with your own values? (yes / no) :
```

Type `yes` and enter your own answer and scores to test it manually.

---

## 🧪 Test Cases Included

| # | Test Name | Expected Result |
|---|---|---|
| 1 | Empty Answer | follow-up → clarification |
| 2 | Wrong Answer | follow-up → correction |
| 3 | Shallow Answer | follow-up → deep_dive |
| 4 | Incomplete Answer | follow-up → clarification |
| 5 | Good Answer | no follow-up |
| 6 | Too Many Attempts | no follow-up (limit reached) |

---

## 🔧 Customize Thresholds

You can change the score limits at the top of `followup_trigger_logic.py`:

```python
CORRECTNESS_LIMIT  = 0.6
DEPTH_LIMIT        = 0.5
COMPLETENESS_LIMIT = 0.7
MAX_ATTEMPTS       = 3
```

---

## 🛠️ Built With

- Python 3
- No external libraries

---

## 📄 License

This project is open source and free to use.
