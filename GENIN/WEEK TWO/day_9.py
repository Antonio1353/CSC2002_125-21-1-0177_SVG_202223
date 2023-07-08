#LEARNING DICTIONARIES
# prog_dict={"name":"my biological true name",
#            "Da Baby":"A rapper in the US"}
# print(prog_dict["Da Baby"])

             # GRADING EXERCISE

# student_scores={
#     "Harry": 81,
#     "Ron":78,
#     "Hermione":99,
#     "Draco":74,
#     "Neville":62,
# }

# student_grades={}
# for key in student_scores:
#     scof=student_scores[key]
# # print(scof)
#     if scof > 90 :
#         student_grades[key]="Outstanding"
#     elif scof > 80 :
#         student_grades[key]="Exceed Expectation"
#     elif scof >71 :
#         student_grades[key]="Acceptable"
#     elif scof < 70 :
#         student_grades[key]="Fail"

# print(student_grades)
   # SECRET AUCTION PROGRAM
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
''')
print("Welcome to the secret Auction Program")
auct= True
prices=[]
highe_st=0
winner=""
while auct:
    Name= input("What is your name\n").upper()
    Bid_price=int(input("How much are you bidding?$"))
    Bid_dit={}
    Bid_dit[Name]=Bid_price
#print(Bid_dit)
    for reis in Bid_dit:
        core=Bid_dit[reis]
        if core > highe_st:
            highe_st=core
            winner=reis
        # prices.append(core)
        # highest=max(prices)



    pe_o=input("are there still more bidders, yes or no").lower()
    if pe_o!="yes":
        auct=False
        print(f"{winner} ,${highe_st}  IS THE WINNER")