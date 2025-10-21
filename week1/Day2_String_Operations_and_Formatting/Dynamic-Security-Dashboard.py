print("🔐 DYNAMIC SECURITY DASHBOARD")
print("="*30)
username = input("add your username:").strip()
total = int(input('Add the total login attempts:'))
successful = int(input('add the successful attempts:'))
score = successful/total

if score >= 0.8:
    status = "✅ Good"
elif score >= 0.6:
    status = "⚠️ Fair"
else:
    status = "❌ Weak"


print(f'User:{username}\n'
      f'Total Attempts:{total}\n'
      f'Successful Logins:{successful}({successful/total:.0%})\n'
      f'Security Score:{successful/total:.0%}\n'
      f'Status:{status}\n')
