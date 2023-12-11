name = input("Whats your name...")
if name == "":
    print("Hello, Stranger")
else:
    print("Hello", name)

word = input("Choose a Password...")
bird = input("Enter Password Again...")
if word == bird:
    print("Password Set...")
else:
    print("Passwords Did Not Match, Please Try Again...")

rat = input("Password must be between 8-12 characters long, Please Choose a Password...")
x = True
while x:
    if (len(rat)<8 or len(rat)>12):
        break
    else:
        print("Password Has Been Set.")
        x = False
        break
if x:
    print("Password Must Be Between 8-12 Characters, Please try Again.")

bad_names = ("apple", "banana", "poop", "jonathan")
print("Please Choose a Password, Passwords Cannot Contain (apple, banana, poop, jonathan)")
bag = input("Please Choose a Password...")
while bag in bad_names:
   dog = input("Password Cannot Be From Mentioned Characters, Please Try Again...")

   if dog not in bad_names:
       print("Password Has Been Set.")
       break
