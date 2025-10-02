# Password Strength Analyser

A Python GUI tool for analyzing and improving password strength, providing real-time feedback, crack-time estimates, and suggestions for stronger passwords. Built using **PySimpleGUI** and deterministic password heuristics.

---

## Features

- **Live password feedback** as you type
- **Password score** display
- **Detailed hints** for improving your password:
  - Length, case, digits, symbols, common words, repeated patterns
- **Actionable steps** for better security:
  - Use multi-factor authentication (MFA)
  - Prefer multi-word passphrases
- **Online and offline attack estimates**
- **Generate strong random passwords**
- **Copy to clipboard** and **clear input**
- **Cross-platform GUI** (Windows/Linux/macOS)

---

## Folder Structure

dongta-security-capstone/
- │
- ├── gui.py # Main GUI application
- ├── analyser.py # Password analysis logic (e.g., using zxcvbn)
- ├── generator.py # Password generator logic
- ├── estimator.py # Crack time estimation logic
- ├── tests/
- │ └── test_feedback.py # Unit tests for password feedback functions
- ├── README.md
- └── requirements.txt # Python dependencies


---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/<your-username>/dongta-security-capstone.git
cd dongta-security-capstone


## create and activate a venv
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

## install dependencies
pip install -r requirements.txt

# Usage

## 1. Run the GUI application:
python gui.py

## 2. Enter a password to analyse:
- Live feedback appears as you type
- Score and actionable hints are displayed
- Online/offline attacks estimates are updated

## 3. Generate strong password using the "Generate Strong" button.
## 4. Copy password to clipboard using the "Copy" button
## 5. Clear the input with the "Clear" button.

# Running tests
python -m unittest discover -s tests

## test password: *HH0wdoIL0veY0u!*

Analyzer / heuristic hints:
 - Length: 17 characters — good.
 - Mixed case: contains both upper and lower case.
 - Contains digits.
 - Contains symbol(s).
 - Looks like a multi-word passphrase — good for memorability and strength.

Actionable steps:
 - Use multi-factor authentication (MFA) where available.

# Dependencies

- PySimpleGUI
- pyperclip
- zxcvbn-python
- Python 3.10+

# Contributing
- Fork the respository
- Create a branc: git checkout -b feature/your-feature
- Commit changes: git commit -m "Add your_feature"
- Push to branch: git push origin feature/your-feature
- Open a pull request
