print("Hi! welcome to card maker")
name = input("your name:").strip()
age = input("your age:").strip()
field = input("your field:").strip()
loves_coding = input("do you love coding?").strip().lower()

# ===============================
try:
    age = int(age)
except ValueError:
    age = 0

loves_coding = True if loves_coding in ["yes", "y", "1", "true"] else False


def print_card(name, age, field, loves_ai):
    lines = [
        f"Name: {name}",
        f"Age: {age}",
        f"Field: {field}",
        f"Loves coding: {'✔' if loves_ai else '✘'}"
    ]
    width = max(len(line) for line in lines) + 2

    print("┌" + "─" * width + "┐")
    for line in lines:
        print("│ " + line.ljust(width - 1) + "│")
    print("└" + "─" * width + "┘")


print_card(name, age, field, loves_coding)
