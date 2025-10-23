print("Threat Level Evaluator")
print("*"*30)
attempts = int(input("Log in attempts:"))
ip_external = input("is IP external? (y\\n) ").strip().lower()
file_size = int(input("file size:"))
print("*"*30)
if (attempts > 5) or (ip_external == "y" and file_size > 10000000):
    print("HIGH")
elif (attempts > 2) and (file_size > 1000000):
    print("MEDIUM")
else:
    print("LOW")
