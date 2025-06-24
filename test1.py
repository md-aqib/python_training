# text = "Hello World"
# print(text)

# 1.
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    spaces = ' ' * (n - i)
    stars = '* ' * i
    print(spaces + stars.strip())

for i in range(n - 1, 0, -1):
    spaces = ' ' * (n - i)
    stars = '* ' * i
    print(spaces + stars.strip())

# 2.
text = input("Enter a text: ")
text = text.lower()
vowels = "aeiou"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels:", count)


# 3.
line = input("Enter a string: ")
result = []
for char in line:
    if char.isupper():
        result.append(char.lower())
    elif char.islower():
        result.append(char.upper())
    # elif char.isdigit():
    #     continue
    # else:
    #     result.append(' ')
output = ''.join(result)
print(output)

# 4.
numbers = []
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)
biggest = max(numbers)
smallest = min(numbers)
average = sum(numbers) / len(numbers)

print(f"Biggest number: {biggest}")
print(f"Smallest number: {smallest}")
print(f"Average: {average}")

# 5.
basicSalary = int(input("Enter your basic salary: "))
da = .15 * basicSalary
hra = .20 * basicSalary
medAllowance = .1 * basicSalary
pf = .12 * basicSalary

otherEarnings = da + hra + medAllowance
deductions = pf
final = basicSalary + otherEarnings - deductions

print(f"Other Earnings: {otherEarnings}")
print(f"Deductions: {deductions}")
print(f"Final Salary: {final}")




