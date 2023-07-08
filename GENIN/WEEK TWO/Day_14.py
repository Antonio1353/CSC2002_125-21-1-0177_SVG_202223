data =[
    {
        'name': 'Instagram',
        'follower_count': 254,
        'description': 'Social media platform',
        'country': 'United States of America'
    },
    {
        'name': 'Adesola Gabriel',
        'follower_count': 215,
        'description': 'Penetration Tester',
        'country': 'Nigeria'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 252,
        'description': 'Musician and Actress',
        'country': 'United States'
    },
    {
        'name': 'Joshephine Adenuga',
        'follower_count': 158,
        'description': 'Mechanical Engineer',
        'country': 'Canada'
    },
    {
        'name': 'Adebowale Adeyemi',
        'follower_count': 125,
        'description': 'Lawyer',
        'country': 'Cameroon'
    },
    {
        'name': 'Onaopepo Ifeoluwa',
        'follower_count': 211,
        'description': 'Data Analyst',
        'country': 'Nigeria'
    }
]
# Display art
import random
def format_data(account):
    """Takes the account and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a {account_descr}, from {account_country}")
def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
score = 0
game_should_continue = True
account_b = random.choice(data)
# Make the game repeatable
while game_should_continue:
    #Generate a random account from the game data.
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
         account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(f"Against B: {format_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B':\n").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    # Clear the screen between rounds.
    ## Use if statement to check if user is correct.
    # Give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You're right! Your current Score is: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final Score is {score}")
