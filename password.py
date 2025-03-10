import random
import string
Special_symbols='!@#$%^&*'
length=int(input("Enter Range of the password:"))
format=input("Type the password is (Easy) (Hard) or (Medium):").lower()
password = []
if (format=='easy'):
    for i in range(length):
        password.append(random.choice(string.ascii_uppercase))
elif (format=='medium'):
    for i in range(length):
        password.append(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits))

elif (format=='hard'):
    for i in range(length):
        password.append(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + Special_symbols))
else:
    print("Invaild Choice....")
random.shuffle(password)
password=''.join(password)
print("Your password is:",password)

