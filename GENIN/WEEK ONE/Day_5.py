#DAY 5
#list
fruits=["APPLE", "PEACH" "PEAR"]
for fruit in fruits:
 print(fruits)


#average_height
print("welcome to average height")
student_heights=input("input list of student heights").split()

total_height=0

for height in student_heights:
    total_height+=height
print(total_height)

number_of_students=0
for student in student_heights:
    number_of_students+=1
print(number_of_students)



#student scores
print("welcome to student score")
student_scores=input("inout a list of student scores")
for n in range(0, len(student_scores)):
    student_scores[n]=int(student_scores[n])
print(student_scores)

highest_score=0
for score in student_scores:
    if score>highest_score:
        highest_score=score
print(f"the highest score in the class is:{highest_score}")



#adding even numbers
print("welcome to adding even numbers")
total=0
for number in range(2, 101, 2):
    total+=number
print(total)

total2=0
for number in range(1, 101):
    if number%2==0:
        total2+=number
print(total2)



#fizzbuzz
print("welcome to fizzbuzz")
for number in range(1, 101):
 if number % 3==0 and number % 5 ==0:
     print("fizzbuzz")
 elif number % 3 ==0:
     print("fizz")
 elif number % 5==0:
     print("buzz")
 else:
     print(number)