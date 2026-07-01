# 10-Days-Python-mini-projects

Welcome to the **10-Days-Python-mini-projects** repository! This project features simple, beginner-friendly Python mini-projects designed to help you practice and build your programming logic day by day.

---

## 🚀 Projects Included

### Day 1: Age Calculator (`Age-calculator.py`)
A straightforward terminal-based application that calculates a user's age based on their birth year and categorizes them into a specific life stage.
*   **Features:**
    *   Calculates exact age using the current year (2026).
    *   Categorizes users dynamically: **Child** (Under 18), **Adult** (18-64), or **Senior Citizen** (65+).

### Day 2: ATM Simulation (`atm_simulation.py`)
A terminal-based program that mimics real-world automated teller machine (ATM) functionalities.
*   **Features:**
    *   **PIN Verification:** Secure entry simulation before accessing the account.
    *   **Balance Inquiry:** Check current funds instantly.
    *   **Cash Deposit & Withdrawal:** Update account balance dynamically with input validation.
    *   **Transaction History:** View previous actions taken during the session.

### Day 3: Simple Calculator (`simple_calculator.py`)
A foundational calculator app to perform basic mathematical operations.
*   **Features:**
    *   Supports addition, subtraction, multiplication, and division.
    *   Handles divide-by-zero errors gracefully.
    *   Looping mechanism to keep calculating without restarting the script.

### Day 4: Student Result Evaluator (`student_result.py`)
A lightweight Python script that automatically processes multi-student rosters to calculate individual course percentages and final **Semester Grade Point Averages (SGPA)** using the standard UGC/AICTE 10-point scale.

*   **Features:**
* **Roster Automation**: Dynamically loops over custom student data structures.
* **Hybrid Layout**: Correctly adapts max marks for courses with or without integrated labs (60 Mid, 70 Sem, 10 Lab).
* **UGC/AICTE Grade Mapping**: Converts final raw percentages straight to official grade points.

## 📐 Grading Scale Reference
* **≥ 90%** ➔ 10 GP | **80-89%** ➔ 9 GP | **70-79%** ➔ 8 GP 
* **60-69%** ➔ 7 GP | **50-59%** ➔ 6 GP | **40-49%** ➔ 5 GP 
* **35-39%** ➔ 4 GP | **< 35%**  ➔ 0 GP (Fail)

### Day 5: Password Generator (`password_generator.py`)
A customizable tool that generates strong, secure, and randomized passwords based on user preferences.
*   **Features:**
    *   **Customizable Length:** Allows users to specify how long they want their password to be.
    *   **Character Inclusion Toggle:** Options to include uppercase letters, lowercase letters, numbers, and special symbols.
    *   **Strength Evaluator:** Gives feedback on how secure the generated password is.

### Day 6: QR Code Generator (`qr_generator.py`)
A handy script that converts text or links into high-quality scannable QR Codes.
*   **Features:**
    *   Converts any string or URL input into a QR code.
    *   Saves the result as a `.png` file directly inside the directory.
    *   Customizable fill and background colors.

### Day 7: Rock Paper Scissors Game (`rock_paper_scissors.py`)
The classic game played against an AI opponent utilizing randomized logic.
*   **Features:**
    *   Interactive command-line gameplay.
    *   Keeps continuous score tracking across multiple rounds.
    *   Robust input validation to handle typos.

### Day 8 (Part 1): Guess the Number (`guess_number.py`)
A fun, interactive game where the player attempts to guess a hidden computer-generated number.
*   **Features:**
    *   Dynamically provides hints (Too High / Too Low).
    *   Tracks the total number of attempts.
    *   Adjustable difficulty modes (Easy, Medium, Hard).

### Day 8 (Part 2): Voter Eligibility Checker (`voter_eligibility.py`)
A verification simulation to check if a user is legally old enough to cast a vote.
*   **Features:**
    *   Checks age limits against regional standards.
    *   Prompts users for country identity validation.
    *   Displays clear registration guidance messages.

### Day 9: Cricket Analysis Report (`cricket_analysis.py`)
A data breakdown script designed to compute and evaluate cricket statistics.
*   **Features:**
    *   Calculates batting averages and strike rates dynamically based on runs, balls, and outs.
    *   Calculates bowling economy rates and match impacts.
    *   Generates a clean terminal-printed statistical summary performance report.

---

## 🛠️ How to Run the Code

1.  **Prerequisites:** Ensure you have [Python](https://www.python.org/) installed on your machine.
2.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Anjankumar-svg/10-Days-Python-mini-projects.git](https://github.com/Anjankumar-svg/10-Days-Python-mini-projects.git)
    cd 10-Days-Python-mini-projects
    ```
3.  **Run a Script:**
    Execute any day's project script via your terminal:
    ```bash
    python Age-calculator.py
    python atm_simulation.py
    python simple_calculator.py
    python student_result.py
    python password_generator.py
    python qr_generator.py
    python rock_paper_scissors.py
    python guess_number.py
    python voter_eligibility.py
    python cricket_analysis.py
    ```

---

## 🤝 Contributing

Contributions are welcome! If you want to optimize the existing code, fix bugs, or add new features:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
