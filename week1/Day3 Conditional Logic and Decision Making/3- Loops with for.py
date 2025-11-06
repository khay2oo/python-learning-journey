# for variable in sequence:
# what is a variable? = the name of I don't know what like (username='khay2oo')
# what it can contain? str(text)|int(1)|float(1.2)|list|dict(dictionary)|bool(T,F)

for i in range(3):  # step (0,1,2)
    print("hi", i)
for o in range(1, 3):  # start, stop (1,2)
    print("hello", o)
for p in range(1, 9, 3):  # start,stop,step,(1,4,7)
    print("!", p)

password = "password"
for u in password:
    print(f'possessing the password: {u}')
for scan in range(20, 24):
    print(f'Scanning port {scan}...')
print("Scan complete.")
