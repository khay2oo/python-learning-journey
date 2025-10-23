attack_ips = []

ip1 = input("Enter attack IP 1:").strip()
attack_ips.append(ip1)

ip2 = input("Enter attack IP 2:").strip()
attack_ips.append(ip2)

ip3 = input("Enter attack IP 3:").strip()

attack_ips.append(ip3)
print("[ATTACK LOG REPORT]")
print(f'total attacks recorded: {len(attack_ips)}\n'
      f'first attack from: {attack_ips[0]}\n'
      f'second attack from: {attack_ips[1]}\n')
if attack_ips[2] == "192.168.1.100":
    print('Is 192.168.1.100 in the log?' + 'True')
else:
    print('Is 192.168.1.100 in the log?' + 'False')
# this is such a bad code, I have hop I'll get better in the future ;)
