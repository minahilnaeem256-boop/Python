# Armstrong Number Checker
print("===== ARMSTRONG NUMBER CHECKER =====")

number=input("enter any number:") 

count=len(number) 
print("number of digits:", count)

total = 0

for i in str(number):
    total += int(i) ** count

if total == int(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")

