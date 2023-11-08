import re
def emailcheck(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    if re.match(regex, email):
        return True
    else:
        return False
    
inp = input()
if emailcheck(inp):
    print("OK")
else:
    print("WRONG")