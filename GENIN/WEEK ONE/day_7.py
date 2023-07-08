import random
word_list=["ardvark", "baboon", "camel"]
chosen_word=random.choice(word_list)
word_length=len(chosen_word)
print(f"psst, the solution is {chosen_word}.")

display=[]
for _ in range(word_length):
    display +="_"


end_of_game= False

while not end_of_game:
 guess = input("guess a letter: ").lower()

 for position in range(word_length):
    letter=chosen_word[position]
    print(f"current position: {position}\n current letter: {letter}\n guessed letter: {guess}")
    if letter ==guess:
        display[position]=letter
 print(display)

 if "_" not in display:
     end_of_game=True
     print("you win")