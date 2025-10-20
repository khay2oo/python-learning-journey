name = "khaytoo"
age = 17
field = "Cyber Security"
loves_learning = True

# ===============================


def print_card(name, age, field, loves_ai):
    lines = [
        f"Name: {name}",
        f"Age: {age}",
        f"Field: {field}",
        f"Loves AI: {'✔' if loves_ai else '✘'}"
    ]
    width = max(len(line) for line in lines) + 2

    print("┌" + "─" * width + "┐")
    for line in lines:
        print("│ " + line.ljust(width - 1) + "│")
    print("└" + "─" * width + "┘")


print_card(name, age, field, loves_learning)
