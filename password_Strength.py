# Simple password checking program. 
# Utilise a dictionary to store values in to check password. 

password_entry = input("Enter Password: ")

strength_check = {}

if len(password_entry) <= 16 and len(password_entry) >= 8:
    strength_check["Length"]= True
else:
    strength_check["Length"] = False

password_number = False
for i in password_entry:
    if i.isdigit():
        password_number = True
strength_check["Number"] = password_number

password_capital = False 

for i in password_entry:
    if i.isupper():
        password_capital =True
strength_check["Capital"] = password_capital


if all(strength_check.values()):
    print("Password Strength: Strong")
else:
    print("Password Stength: Weak")
