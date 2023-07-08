#day 2
# string
print("123" + "345")

#integer
print(123 + 345)

#float
3.14159

#boolean
True
False

num_char = len(input("what is your name?"))
new_num_char = str(num_char)
print("your name has " + new_num_char +" characters.")

a = float(123)
print(type(a))

print(70 + float("100.5"))

two_digit_number = input("type a two digit number")
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
print(first_digit)
print(second_digit)
result = first_digit + second_digit
print(result)

print(3+5)
print(7-4)
print(3*2)
print(6/3)
print(2**3)

#PEDMAS
print(3*3+3/3-3)
print(3*(3+3)/3-3)

height = int(input("enter your height in m:"))
weight = int(input("enter your weight in kg:"))
bmi = weight/height**2
print(bmi)

print("welcome to the tip calcultor")
bill=float(input("what was the total bill? $\n"))

tip=int(input("what percentage tip would you like to give? 10, 12, or 15?\n"))

people=int(input("how many people to split the bill?\n"))

tip_as_percent=tip/100

total_tip_amount=bill*tip_as_percent

total_bill=bill+total_tip_amount

bill_per_person=total_bill/people

final_amount=round(bill_per_person,2)

print(f"each person shhould pay: ${final_amount}")