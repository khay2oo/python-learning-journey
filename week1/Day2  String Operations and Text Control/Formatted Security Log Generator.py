
username = "khay2oo"
ip = "192.168.1.100"
attempts = 5
status = "Blocked"
title = "[SECURITY ALERT]"
line = len(title)  # count the number of characters\objects inside a group
print(title)
print("="*line)  # "A"*10 => AAAAAAAAAA | A*10❌ | "A"*"10"❌ | "A"*9.9❌
# \n => New line
# \t => tab (space)
# \r => carriage Return == "world\rhello"= helloworld
# \" => quote => "\"hi\""= "hi"
print(f"User:\t{username}", f'IP:\t{ip}',
      f'Attempts:\t{attempts}', f'Status:\t{status}', sep="\n")
# the defult is end="\n" so if we delete that the second print will be in the same line
print("hello", end=" ")
# sup is the space between the words and it can be any thing
print("world", "!", sep="-")
