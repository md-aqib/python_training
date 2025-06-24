# 1.
# import re
# def login():
#     password = input("Enter password: ")
#     splChars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
#     specialPattern = f"[{re.escape(splChars)}]"
#     if (len(password) >= 8 and
#         re.search(r'[A-Z]', password) and
#         re.search(r'[a-z]', password) and
#         re.search(r'\d', password) and
#         re.search(specialPattern, password)):
#         print("Password is valid!")
#     else:
#         suggestion = "Aa1!" + "xY2@"
#         print("Invalid password.")
#         print("Suggested secure password:", suggestion)
# login()

# 2.
# from datetime import datetime
# birthdate = input("Enter Birth Date in yyyy-mm-dd format: ")
# def bdayCheck(birthdate):
#     try:
#         b = datetime.strptime(birthdate, "%Y-%m-%d")
#     except ValueError:
#         return "Invalid date format. Please use yyyy-mm-dd."
#     today = datetime.today()
    
#     try:
#         thisBday = b.replace(year=today.year)
#     except ValueError:
#         thisBday = datetime(today.year, 2, 28)

#     if thisBday.date() == today.date():
#         return "Happy Birthday!", (b.month, b.day)

#     if thisBday < today:
#         try:
#             nextBday = b.replace(year=today.year + 1)
#         except ValueError:
#             nextBday = datetime(today.year + 1, 2, 28)
#         daysLeft = (nextBday - today).days
#     else:
#         daysLeft = (thisBday - today).days

#     return f"{daysLeft} days left", (b.month, b.day)
# print(bdayCheck(birthdate))

# 3.
# import random
# def genQue():
#     ops = ['+', '-', '*', '//']
#     a = random.randint(1, 10)
#     b = random.randint(1, 10)
#     op = random.choice(ops)
#     question = f"{a} {op} {b}"
#     answer = eval(question)
#     return question, answer

# def mathQuiz():
#     questions = {}
#     score = 0
#     noOfQues = 5

#     for i in range(1, noOfQues + 1):
#         q, a = genQue()
#         questions[q] = a
#         print(f"Question {i}: {q} = ?")
#         try:
#             userAns = int(input("Your answer: "))
#         except ValueError:
#             print("Invalid input! Counting as wrong.")
#             userAns = None

#         if userAns == a:
#             print("Correct!\n")
#             score += 1
#         else:
#             print(f"Wrong! The correct answer is {a}.\n")
#     print(f"You got {score} out of {noOfQues} correct!")
# mathQuiz()


# 4.
# def calcNum(numbers):
#     total = sum(numbers)
#     mean = total / len(numbers)
#     maxVal = max(numbers)
#     minVal = min(numbers)
    
#     variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
#     standardDeviation = variance ** 0.5

#     evenCount = sum(1 for x in numbers if x % 2 == 0)
#     oddCount = len(numbers) - evenCount

#     return mean, maxVal, minVal, standardDeviation, evenCount, oddCount
# numbers = []
# print("Enter 10 numbers:")
# while len(numbers) < 10:
#     try:
#         num = float(input(f"Number {len(numbers)+1}: "))
#         numbers.append(num)
#     except ValueError:
#         print("Invalid input. Please enter a number.")
# mean, maxVal, minVal, standardDeviation, even, odd = calcNum(numbers)

# print(f"Mean: {mean:.2f}")
# print(f"Max: {maxVal}")
# print(f"Min: {minVal}")
# print(f"Standard Deviation: {standardDeviation:.2f}")
# print(f"Even numbers: {even}")
# print(f"Odd numbers: {odd}")


# 5.
def checkScores(scores):
    highScorers = []
    total = 0
    for name in scores:
        mark = scores[name]
        total += mark
        if mark > 90:
            highScorers.append(name)
    average = total / len(scores)
    return highScorers, average
scores = {}

print("Enter student names and their marks out of 100.")
print("Type 'done' to stop.\n")

while True:
    name = input("Student name: ")
    if name.lower() == 'done':
        break
    try:
        mark = float(input("Score: "))
        if 0 <= mark <= 100:
            scores[name] = mark
        else:
            print("Please enter a score between 0 and 100.")
    except:
        print("Please enter a valid number.")
if scores:
    topStudents, avg = checkScores(scores)
    print(f"Average score: {avg:.2f}")
    print("Students who scored more than 90:")
    for student in topStudents:
        print(student)
else:
    print("No data entered.")



