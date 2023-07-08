#DEBUGGING
## Describe Problem
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")
my_function()

from random import randint
dice_imgs = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(0,5)
print(dice_imgs[dice_num])
year = int(input("What's your year of birth?\n"))
if year > 1980 and year < 1994:
    print("You are a Millenial.")
elif year >= 1994:
    print ("You are a Gen Z.")
age = int(input("How old are you?\n"))
if age > 18:
    print(f"You can drive at age {age}.")
elif age < 18:
    print(f"You are underage, You can't drive at age {age}")
#    #print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of words per paage:\n"))
word_per_page = int(input("Number of words per page:"))
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")
print(total_words)

# Use a Debugger
def mutate(a_list):
    b_list = []
    for item in b_list:
      new_item = item * 2
      b_list.append(new_item)
    print(b_list)
mutate([1,2,3,4,5,6,8,13])
number = int(input("Which number do you want to check?\n"))
if number %2 == 0:
    print("This is an even number")
else:
    print("This is an odd number.")

year = int(input("Which year do you want to check?\n"))
if year %4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year.")
        else:
            print("Not Leap Year.")
    else:
        print("Leap Year.")
else:
    print("Not leap Year.")

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)