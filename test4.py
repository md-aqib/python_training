# 1.
# class PetShop:
#     def __init__(self):
#         self.petList = []

#     def addPet(self, petId, name, petType, breed, age, vaccinated):
#         for pet in self.petList:
#             if pet['petId'] == petId:
#                 print("Error: Pet ID already exists.")
#                 return
#         pet = {
#             'petId': petId,
#             'name': name,
#             'type': petType,
#             'breed': breed,
#             'age': age,
#             'vaccinated': vaccinated
#         }
#         self.petList.append(pet)
#         print("Pet added successfully!")

#     def showPet(self, petId):
#         for pet in self.petList:
#             if pet['petId'] == petId:
#                 print(pet)
#                 return
#         print("Pet not found!")

#     def updatePet(self, petId, field, newValue):
#         for pet in self.petList:
#             if pet['petId'] == petId:
#                 if field in pet:
#                     pet[field] = newValue
#                     print("Pet updated!")
#                 else:
#                     print("Field not found!")
#                 return
#         print("Pet not found!")

#     def deletePet(self, petId):
#         for pet in self.petList:
#             if pet['petId'] == petId:
#                 self.petList.remove(pet)
#                 print("Pet deleted!")
#                 return
#         print("Pet not found!")

#     def filterPets(self, field, value):
#         found = False
#         for pet in self.petList:
#             if field in pet:
#                 petValue = pet[field]
#                 if isinstance(petValue, str) and isinstance(value, str):
#                     if petValue.lower() == value.lower():
#                         print(pet)
#                         found = True
#                 else:
#                     if petValue == value:
#                         print(pet)
#                         found = True
#         if not found:
#             print("No pets found with that criteria.")

# shop = PetShop()
# shop.addPet(1, "Buddy", "Dog", "Golden Retriever", 4, True)
# shop.addPet(2, "Kitty", "Cat", "Persian", 2, False)
# shop.addPet(3, "Rex", "Dog", "German Shepherd", 5, True)
# shop.showPet(2)
# shop.updatePet(3, "age", 6)
# shop.deletePet(1)
# shop.filterPets("type", "Dog")
# shop.filterPets("vaccinated", True)


# 2.
# import re
# def isValidEmail(email):
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     if re.match(pattern, email):
#         return True
#     else:
#         return False

# print(isValidEmail("user@abccorp.com"))
# print(isValidEmail("user@.com"))
# print(isValidEmail("john.doe@example.co.uk"))
# print(isValidEmail("user@@domain.com"))


# 3.
# import re
# def isValidS3BucketName(bucketName):
#     pattern = r'^[a-z0-9][a-z0-9-]{8,13}[a-z0-9]$'
#     if re.match(pattern, bucketName):
#         return True
#     else:
#         return False
# print(isValidS3BucketName("my-bucket-123"))
# print(isValidS3BucketName("MyBucket!"))
# print(isValidS3BucketName("-mybucket123"))
# print(isValidS3BucketName("bucket-"))
# print(isValidS3BucketName("bucketnamewithtoolong"))

# 4.
# def isValidCIDR(cidrBlock):
#     if '/' not in cidrBlock:
#         return False

#     ipPart, prefixPart = cidrBlock.split('/')
#     if not prefixPart.isdigit():
#         return False
#     prefix = int(prefixPart)
#     if prefix < 0 or prefix > 32:
#         return False
#     ipParts = ipPart.split('.')
#     if len(ipParts) != 4:
#         return False
#     for part in ipParts:
#         if not part.isdigit():
#             return False
#         number = int(part)
#         if number < 0 or number > 255:
#             return False
#     return True
# print(isValidCIDR("10.0.0.0/16"))
# print(isValidCIDR("192.168.1.1/24"))
# print(isValidCIDR("256.0.0.0/24"))
# print(isValidCIDR("10.0.0/16"))
# print(isValidCIDR("10.0.0.0/33"))


# 5.
class TicketSystem:
    def __init__(self):
        self.ticketList = []

    def createTicket(self, ticketId, issueDescription, priorityLevel, status="Open"):
        if priorityLevel < 1 or priorityLevel > 5:
            raise ValueError("Priority must be between 1 and 5.")

        ticket = {
            "ticketId": ticketId,
            "issueDescription": issueDescription,
            "priorityLevel": priorityLevel,
            "status": status
        }

        self.ticketList.append(ticket)
        print(f"Ticket {ticketId} created.")

    def readTicket(self, ticketId):
        for ticket in self.ticketList:
            if ticket["ticketId"] == ticketId:
                return ticket
        raise LookupError(f"Ticket {ticketId} not found.")

    def updateTicket(self, ticketId, issueDescription=None, priorityLevel=None, status=None):
        for ticket in self.ticketList:
            if ticket["ticketId"] == ticketId:
                if issueDescription:
                    ticket["issueDescription"] = issueDescription
                if priorityLevel is not None:
                    if priorityLevel < 1 or priorityLevel > 5:
                        raise ValueError("Priority must be between 1 and 5.")
                    ticket["priorityLevel"] = priorityLevel
                if status:
                    ticket["status"] = status
                print(f"Ticket {ticketId} updated.")
                return
        raise LookupError(f"Ticket {ticketId} not found.")

    def deleteTicket(self, ticketId):
        for i in range(len(self.ticketList)):
            if self.ticketList[i]["ticketId"] == ticketId:
                self.ticketList.pop(i)
                print(f"Ticket {ticketId} deleted.")
                return
        raise LookupError(f"Ticket {ticketId} not found.")

system = TicketSystem()
try:
    system.createTicket(1, "Keyboard not working", 3)
    system.createTicket(2, "Cannot login", 7)
except ValueError as e:
    print("Error:", e)
try:
    print(system.readTicket(1))
    print(system.readTicket(5))
except LookupError as e:
    print("Error:", e)
try:
    system.updateTicket(1, status="Resolved")
    system.updateTicket(1, priorityLevel=0)
except (LookupError, ValueError) as e:
    print("Error:", e)
try:
    system.deleteTicket(2)
except LookupError as e:
    print("Error:", e)


