# 1.
# class Account:
#     def __init__(self, accNum, holder, accType, balance, status):
#         self.accNum = accNum
#         self.holder = holder
#         self.accType = accType
#         self.balance = balance
#         self.status = status  # 'active', 'closed', 'inactive'

#     def show(self):
#         print(f"{self.accNum} | {self.holder} | {self.accType} | ₹{self.balance} | {self.status}")
# accounts = []

# def createAccount(accNum, holder, accType, balance, status):
#     acc = Account(accNum, holder, accType, balance, status)
#     accounts.append(acc)
#     print("Account created.\n")

# def showAll():
#     print("\nAll Accounts:")
#     for acc in accounts:
#         acc.show()

# def updateBalance(accNum, amount):
#     for acc in accounts:
#         if acc.accNum == accNum:
#             if acc.status == "active":
#                 acc.balance += amount
#                 print("Balance updated.\n")
#             else:
#                 print("Cannot update. Account is not active.\n")
#             return
#     print("Account not found.\n")

# def deleteAccount(accNum):
#     for acc in accounts:
#         if acc.accNum == accNum:
#             if acc.status in ["closed", "inactive"]:
#                 accounts.remove(acc)
#                 print("Account deleted.\n")
#             else:
#                 print("Cannot delete. Account is active.\n")
#             return
#     print("Account not found.\n")

# createAccount(1, "Alice", "Savings", 1000, "active")
# createAccount(2, "Bob", "Current", 2000, "inactive")
# showAll()
# updateBalance(1, 500)
# updateBalance(2, 300)
# deleteAccount(2)
# deleteAccount(1)
# showAll()


# 2.
# class Product:
#     def __init__(self, id, name, category, price, stockStatus):
#         self.id = id
#         self.name = name
#         self.category = category
#         self.price = price
#         self.stockStatus = stockStatus # inStock, outOfStock
#     def show(self):
#         print(f"{self.id} | {self.name} | {self.category} | ₹{self.price} | {self.stockStatus}")
# products = []

# def createProduct(id, name, category, price, stockStatus):
#     prod = Product(id, name, category, price, stockStatus)
#     products.append(prod)
#     print("Product created")

# def showAll():
#     for product in products:
#         product.show()

# def updateProduct(id, name, category, price, stockStatus):
#     for product in products:
#         if(product.id == id):
#             print(f"Product {product.name} is updating...\n")
#             product.name = name
#             product.category = category
#             product.price = price
#             product.stockStatus = stockStatus
#             return
#     print("Product not found")          

# def deleteProduct(id):
#     for product in products:
#         if(product.id == id):
#             products.remove(product)
#             print(f"Product {product.name} deleted")
#             return
#     print("Product not found")

# createProduct(1, "prod1", "cat1", 100, "inStock")
# createProduct(2, "prod2", "cat2", 200, "outOfStock")
# showAll()
# updateProduct(1, "prod3", "cat3", 1000, "outOfStock")
# updateProduct(2, "prod4", "cat4", 1500, "inStock")
# showAll()
# deleteProduct(1)
# showAll()


# 3.
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#     def makeSound(self):
#         print("This animal makes a sound.")

# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name, "Dog")
#     def makeSound(self):
#         print(f"{self.name} says: Woof! Woof!")

# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name, "Cat")
#     def makeSound(self):
#         print(f"{self.name} says: Meow!")

# class Bird(Animal):
#     def __init__(self, name):
#         super().__init__(name, "Bird")
#     def makeSound(self):
#         print(f"{self.name} says: Chirp! Chirp!")

# dog = Dog("Dog")
# cat = Cat("Cat")
# bird = Bird("Cat")
# dog.makeSound()
# cat.makeSound()
# bird.makeSound()

# 4.
# class BankAccount:
#     def __init__(self, accountNum, holderName, balance=0):
#         self.accountNum = accountNum
#         self.holderName = holderName
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"₹{amount} deposited. New balance: ₹{self.balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance.")
#         elif amount <= 0:
#             print("Withdraw amount must be positive.")
#         else:
#             self.balance -= amount
#             print(f"₹{amount} withdrawn. New balance: ₹{self.balance}")

#     def checkBal(self):
#         print(f"Account Balance: ₹{self.balance}")

# class SavingsAccount(BankAccount):
#     def __init__(self, accountNum, holderName, balance=0, interestRate=0.03):
#         super().__init__(accountNum, holderName, balance)
#         self.interestRate = interestRate  # default: 3%

#     def applyInt(self):
#         interest = self.balance * self.interestRate
#         self.balance += interest
#         print(f"Interest of ₹{interest:.2f} applied. New balance: ₹{self.balance:.2f}")

# account = SavingsAccount("SB12345", "Alice", 1000, 0.05)
# account.checkBal()
# account.deposit(500)
# account.withdraw(200)
# account.applyInt()
# account.checkBal()


# 5.
class Employee:
    def __init__(self, employeeId, name, designation, salary):
        self.employeeId = employeeId
        self.name = name
        self.designation = designation
        self.salary = salary
        self.bonus = 0
        self.tax = 0
    def calculateBonus(self):
        raise NotImplementedError("Subclass must implement bonus calculation.")
    def applyTax(self):
        raise NotImplementedError("Subclass must implement tax calculation.")
    def generatePayslip(self):
        netSalary = self.salary + self.bonus - self.tax
        print(f"Payslip for {self.name} (ID: {self.employeeId})")
        print(f"Designation: {self.designation}")
        print(f"Base Salary: ₹{self.salary:.2f}")
        print(f"Bonus: ₹{self.bonus:.2f}")
        print(f"Tax Deducted: ₹{self.tax:.2f}")
        print(f"Net Salary: ₹{netSalary:.2f}")

class FullTimeEmployee(Employee):
    def calculateBonus(self):
        self.bonus = self.salary * 0.10
    def applyTax(self):
        taxableIncome = self.salary + self.bonus
        self.tax = taxableIncome * 0.20

class PartTimeEmployee(Employee):
    def calculateBonus(self):
        self.bonus = self.salary * 0.05
    def applyTax(self):
        taxableIncome = self.salary + self.bonus
        self.tax = taxableIncome * 0.10

ftEmp = FullTimeEmployee(101, "Alice", "Manager", 50000)
ptEmp = PartTimeEmployee(102, "Bob", "Consultant", 20000)
ftEmp.calculateBonus()
ftEmp.applyTax()
ftEmp.generatePayslip()
ptEmp.calculateBonus()
ptEmp.applyTax()
ptEmp.generatePayslip()




