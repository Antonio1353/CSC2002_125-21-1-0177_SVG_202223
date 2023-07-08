#day 3
#rollercoaster
print("welcome to the rollercoaster")
height=int(input("what is your height in cm?\n"))
if height>=120:
 print("you can ride the rollercoaster")
else: 
  print("sorry, you have to grow taller before you can ride")


#modulo operation
print("welcome to modulo operation")
number=int(input("which number do you want to change?\n"))
if number%2==0:
 print("this is a even number")
else:
 print("this is an odd number")


#bmi
print("welcome to bmi")
height=float(input("enter your height in m:\n"))
weight=float(input("enter your weight in kg:\n"))
bmi=round(weight/height**2)
if bmi<18.5:
  print(f"your bmi is {bmi}, you are under weight")
elif bmi<25:
  print(f"your bmi is {bmi}, you have a normal weight")
elif bmi<30:
   print(f"your bmi is {bmi} you are over weight")
elif bmi<35:
  print(f"your bmi is {bmi}, you are obese")
else:
  print(f"your bmi is {bmi}, you are clinically obese")


#leap year
print("welcome to leap year check")
year=int(input("which year do you want to check?\n"))
if year%4==0:
  if year%100==0:
         if year%400==0:
          print("leap year")
         else:
          print("not leap year")
  else:
      print("leap year")
else:
  print("not leap year")



#pizza order
print("welcome to pizza order")
size=input(("what size pizza do uou want? s, m, or l"))
add_pepperoni=input("do you want pepperoni? y or n")
extra_cheese=input("do you want extra cheese? y or n")
bill=0
if size=="s":
 bill+=15
elif size=="m":
 bill+=20
else:
  bill+=25
if add_pepperoni=="y":
 if size=="s":
   bill+=2
 else:
   bill+=3
if extra_cheese=="y":
  bill+=1
print(f"your final bill is ${bill}")