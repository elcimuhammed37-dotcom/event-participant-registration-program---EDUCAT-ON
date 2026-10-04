#REGÝSTRATÝON SECTÝON

firstName=input("Please enter your first name: ")
lastName=input("Please enter your last name: ")
contactNumber=input("Please enter your contact number: ")

firstName=firstName.title().strip()

lastName=lastName.title().strip()

fullName=f"{firstName} {lastName}"

contactNumber=contactNumber.replace(" ","")

print("Congratulations ! your registration was successful")
print(f"Welcome {fullName}! saved contact number : {contactNumber}")




