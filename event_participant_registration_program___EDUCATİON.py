
#GLOBAL VERIABLE ASSIGMENT

clientWorkshopSet=set()
fullNameList= []
contactNumberList=[]
recordMainDictionary= dict()

#FUNCTION ASIGMENT SECTION
def record_Function():

    firstName= None
    while firstName!="exit":
        print("Welcome to registration section \n")
        firstName=input("Please enter your first name (write \'exit\' for exit ): ")
        firstName=firstName.lower()
    
        if firstName=="exit":
            print("registration part was completed")
            continue

        else:
            lastName=input("Please enter your last name: ")
            clientWorkshop=input("please enter the worshop you are registered for: ")
            contactNumber=input("Please enter your contact number: ")

            firstName=firstName.title().strip()
            clientWorkshop=clientWorkshop.title().strip()
            lastName=lastName.title().strip()

            fullName=(firstName,lastName)
            fullNameList.append(fullName)

            clientWorkshopSet.add(clientWorkshop)

            contactNumber=contactNumber.replace(" ","")
            contactNumberList.append(contactNumber)
            recordMainDictionary={contact:name for contact,name in zip(contactNumberList,fullNameList) }
    else:
        lastState= "Registration process has been completed" if len(fullNameList)>0 else "no recording was made"
        print(lastState)
    

def delete_Record_Function():
    search= input("enter the contact number you wanna find and delete please: ")
    if search_Function(recordMainDictionary,search):
        print(f"{search} has been found. ")
        print(" data has been deleted")
    else:
        print(f"Unfortunately! {search} was not found \n")
     
# SEARCH REGÝSTRATÝON
def show_record_Function():
    print("Congratulations ! registration part was successful")
    for i ,(key,value) in enumerate(recordMainDictionary.items(),start=1):
        print(f"{i}. Name -> {value[0],value[1]} Number -> {key} ")
    for name in vipMembers:
        print(f"VIP members name: {name}  ")

    print(clientWorkshopSet)

def search_Function(myDict,myKey):
    return myDict.pop(myKey,None) is not None

#MAÝN SCOPE

record_Function()

delete_Record_Function()

vipMembers=[(name[0] +" VIP") for name in recordMainDictionary.values()]

show_record_Function()