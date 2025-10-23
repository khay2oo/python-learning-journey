username = input('enter username:') .strip() .lower()
attempts = int(input('how many login attempts:'))
hour = int(input("at what hour:"))

if username == "admin" and attempts <= 3 and 6 <= hour <= 22:
    print("✅ Full access granted")
elif username == "admin" and attempts <= 2:
    print("✅ Standard access")
else:
    print("❌ Access denied: Too many attempts or invalid user")
