username = input("What is your name?").strip()
age = int(input("How old are you?"))
field = input("What is your field?").strip()
love_python = input("Do you love python? (yes/no):").strip().lower()
answer = love_python in ["yes", "y", "1", "true"]

print("👤 Personal Info Card")
print("="*30)
print(f'Name:{username:<15}')
print(f'Age:{age:<15}')
print(f'Field:{field:<15}')
print(f'Loves Python:{'✔' if answer else '✘'}')
