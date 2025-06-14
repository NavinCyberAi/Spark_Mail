import sys

if len(sys.argv) <2:
    print("Usage: Python Generated_email.py 'First Name and Last Name'")
    sys.exit()


full_name= " ".join(sys.argv[1:])
print(full_name)

email= full_name.lower().replace(" ", ".") + "@company.com"

print("\n ---Profile---")
print("Full Name:", full_name)
print("Generated_Email:", email)

