import re

# ask user for a password
password = input("Enter your password: ").strip()

# track score for strength
score = 0

# length check
if len(password) >= 8:
    score += 1
else:
    print("Weak: Password must be at least 8 characters long.")

# uppercase letter check
if re.search(r"[A-Z]", password):
    score += 1
else:
    print("Weak: Password must contain at least one uppercase letter.")

# lowercase letter check
if re.search(r"[a-z]", password):
    score += 1
else:
    print("Weak: Password must contain at least one lowercase letter.")

# digit check
if re.search(r"[0-9]", password):
    score += 1
else:
    print("Weak: Password must contain at least one digit.")

# special character check
if re.search(r"[!@#$%^&*()_+]", password):
    score += 1
else:
    print("Weak: Password must contain at least one special character.")

# final strength verdict
if score == 5:
    print("Strong password! ✅")
elif 3 <= score < 5:
    print("Medium strength password ⚠️")
else:
    print("Weak password ❌")
