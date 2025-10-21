import time
base_name = "user"
# Generate a unique number based on current time
number = int(time.time()) % 1000
domain = "testlab.local"
print("Credential:", base_name + str(number), "|", "Email:" +
      base_name + "@" + domain, "|", "Temp Password:"+"pass"+str(number)+"!")
