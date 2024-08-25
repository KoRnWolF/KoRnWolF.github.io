from game_data import data
from random import randint
from logo import logo, logo_vs
from os import system

candidate_a = data[randint(0, len(data))]
cont_flag = True
score = int()

def check_followers():
    """Checks follower amount between two keys and returns the bigger option A or B"""
    a_followers = candidate_a['follower_count']
    b_followers = candidate_b['follower_count']

    if a_followers > b_followers:
        check = "a"
        return check
    if b_followers > a_followers:
        check = "b"
        return check
    
def end_game():
    system('cls')
    print(logo)
    print(f"You are wrong. Final Score : {score}")
    exit()

def check_answer(choice, largest_follower, candidate_b, candidate_a):#SHIT code
    """checks the player choice against the largerst_follower variable, and changes candidate a to candidate b for next round if correct"""
    if choice == largest_follower:
        print("You are right")
        if choice == "a":
            candidate_a = candidate_b
            print(candidate_a)
            return candidate_a

        if choice == "b":
            candidate_a = candidate_b
            print(candidate_a)
            return candidate_a
        
    else:
        end_game()

while cont_flag:
    system('cls')
    candidate_b = data[randint(0, len(data) -1)]
    if candidate_a == candidate_b:
        candidate_b = data[randint(0, len(data) -1)]
        
    print(logo)
    if score > 0:
        print(f"You're right! current score: {score}")

    print(f"compare A : {candidate_a['name']}, {candidate_a['description']}, {candidate_a['country']}")
    print(logo_vs)
    print(f"compare B : {candidate_b['name']}, {candidate_b['description']}, {candidate_b['country']}")

    largest_follower = check_followers()
    
    choice = input("Who has more followers? Type 'A' or 'B':").lower()
    candidate_a = check_answer(choice, largest_follower, candidate_b, candidate_a)
    if choice == largest_follower:

        score += 1

