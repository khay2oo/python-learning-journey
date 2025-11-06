# if condition: if true
# else: if false

# and => 1,0=0
# or => 1,0=1
# not=> 1=0
# "",0,{},[], ,= False
# in=> if inside a collection | not in
# is => a=[1,2] b=a c=[1,2] -> a is b =true, a is c = false

username = "guest_khay2oo"
login_attempts = 5

if username == "admin":
    print("Full Access")
elif "guest" in username:
    print("Guest access")
elif login_attempts <= 3:
    print("Limited Access")
else:
    print("Access Denied")
