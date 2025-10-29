name = input("name:")  # str
age = int(input("age:"))  # str => int 1
score = float(input("score:"))  # str => float 1.0
answer = input("do you love python?").strip().lower()
# strip(delete all spaces)
# lower (make all letters in lower case)
love_python = answer in ["yes", "y", "1", "true"]
# if answer input= yes or y or 1 or true then print true

# =================f-string=====================
# f' text {Variables:format_spec}
# ----------text alignment-------------
print(f'text alignments are: L(<),R(>), center(^)')
print(f'{name:<10}')
print(f'{name:>10}')
print(f'{name:^10}')
# ------------Operations---------------
print(f'age:{age+1}')
print(f'age:{age-1}')
print(f'age:{age/1}')
print(f'age:{age*1}')
# ect...
print(f'score:{score:2f}')  # 0.00 \ e.g 87.98
print(f'score:{score:3f}')  # 0.000 \ e.g 87.980
# ---
print(f'score:{score:.0%}')  # 0% \ e.g 0.87=> 87%
# ---
print(f'love python: {'✔' if love_python else '✘'}')
