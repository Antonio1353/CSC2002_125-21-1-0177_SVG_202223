#day4
#mersenne twister
print("welcome to mersenne twister")
import random

randominteger=random.randint(1, 10)
print(randominteger)

randomfloat=random.random()*5
print(randomfloat)


#data structure

states_of_america=["Delware", "Pennysvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hamsphire",
"Virnia"]
print(states_of_america)


import random
test_seed=int(input("create a seed number:"))
random.seed(test_seed)
namesAsCSV=input("give me everybody`s names, separated by a comma\n")
names=namesAsCSV.split(",")
num_items=len(names)
random_choice=random.randint(0, num_items-1)
person_who_will_pay=names[random_choice]
print(person_who_will_pay + "is going to buy the meal today!")


#treasure map
row1=["📋" "📋" "📋"]
row2=["📋" "📋" "📋"]
row3=["📋" "📋" "📋"]
map=[row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("where do you want to put the treasure?")

horizontal=position[0]
vertical=position[1]

selected_row=map[vertical-1]
selected_row[horizontal-1]="X"