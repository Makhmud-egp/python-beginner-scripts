# Password Strength Checker

A simple Python program that checks the strength of a password based on the following criteria:
- Minimum length of **8 characters**
- At least **1 uppercase letter**
- At least **1 lowercase letter**
- At least **1 digit**
- At least **1 special character** (`!@#$%^&*()_+`)

## 🚀 How to Run
1. Make sure you have Python installed (`python --version`).
2. Save the script as `password_checker.py`.
3. Run it from the terminal:
   ```bash
   python password_checker.py

## 📌 Example
- Enter your password: mypass
Weak: Password must be at least 8 characters long.
Weak: Password must contain at least one uppercase letter.
Weak: Password must contain at least one digit.
Weak: Password must contain at least one special character.
❌ Weak password! Please try again.

Enter your password: MyPass123!
✅ Strong password!
