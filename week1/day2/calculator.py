print("choose an operation:")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
print("5. personage")

choice = input("operation:")
choice = int(choice)
x = float(input("enter x:"))
y = float(input("enter y:"))

if choice == 1:
    print(f"{x}+{y}={x+y}")
elif choice == 2:
    print(f"{x}-{y}={x-y}")
elif choice == 3:
    print(f"{x}×{y}={x*y}")
elif choice == 4:
    print(f"{x}÷{y}={x/y}")
elif choice == 5:
    print(f"{x}of{y}={(y/x)*100}%")
else:
    print("Invalid choice")
