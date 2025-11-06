# I didn't do this I gust used it for learning purposes
# Password Security Auditor
# A practical tool to evaluate password strength
# Combines: variables, input, string methods, for loops, conditionals, f-strings, and formatting

# 1. Collect password (Day 1: input, strip)
password = input("Enter your password: ").strip()

# 2. Validate length (Day 2: len())
min_length = 8
is_long_enough = len(password) >= min_length

# 3. Initialize flags (Day 3: variables for logic)
has_upper = False
has_lower = False
has_digit = False

# 4. Analyze each character (Day 3: for loop + string methods)
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True

# 5. Calculate strength score (Day 3: boolean arithmetic)
score = has_upper + has_lower + has_digit

# 6. Determine strength level (Day 3: if/elif/else)
if score == 3 and is_long_enough:
    strength = "Strong"
elif score >= 2 and is_long_enough:
    strength = "Medium"
else:
    strength = "Weak"

# 7. Generate icon using ternary operator (Day 3: conditional expression)
length_icon = "✅" if is_long_enough else "❌"
strength_icon = "✅" if strength == "Strong" else "⚠️" if strength == "Medium" else "❌"

# 8. Create dynamic title and border (Day 2: string repetition)
title = "🔐 PASSWORD SECURITY AUDIT"
border = "=" * len(title)

# 9. Build and print the full report (Day 1 & 2: f-strings, \n)
report = f"""{title}
{border}
Password: {password}
Length:   {len(password)} characters {length_icon}
Strength: {strength} {strength_icon}

{"✅ Strong password detected." if strength == "Strong" else "⚠️ Consider improving your password." if strength == "Medium" else "❌ Warning: Password is too short and/or weak!"}"""

print(report)
