# https://www.youtube.com/watch?v=poB7eafmSbk
# How Does Python Validate An Email Address?
# Bring in the library
#  that we need. 
import re
# We'll use this 
#  Regular Expression 
#  throughout this program.
# It matches an email address.
pattern = r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$"
email = "hoosier@mailbox.com"
if re.match(pattern, email):
    print(f"{email} is Valid")
else:
    print(f"{email} is Invalid")
# Try an example that is invalid.
# We omit the TLD on the address.
email = "hoosier@mailbox"
if re.match(pattern, email):
    print(f"{email} is Valid")
else:
    print(f"{email} is Invalid")
# Try an example that is invalid.
# We omit the user name.
email = "@mailbox.com"
if re.match(pattern, email):
    print(f"{email} is Valid")
else:
    print(f"{email} is Invalid")
# What if there's a leading space?
# What will our pattern do?
email = " foo@mailbox.com"
if re.match(pattern, email):
    print(f"{email} is Valid")
else:
    print(f"{email} is Invalid")
