#!/usr/bin/env python3

print("Welcome to Video Game Trivia!")
print("You will be asked a series of 10 multiple choice questions. The number of correct answers you get will decide how much of a video game historian you are")

ready = " "

while ready != "Y" and ready != "N":
    ready = input("Ready to begin? Enter press Y or N: ").upper()

while True:
    if ready == "N":
        print("Sorry you don\'t want to play. Maybe some other time :(")
        break

    score = 0

    answers = ['A', 'B', 'C', 'D']
    
    question = 1
    answer1 = " "
    while answer1 not in answers:
        answer1 = input(f"Question: {question}\nWhat is the best selling videogame of all time?\nA: Mario Kart\nB: Battle Toads\nC: Minecraft\nD: Skyrim\n").upper()

        if answer1 == "C":
            print("Correct!")
            score +=1
            print(f"Your score is {score} out of {question}")
            question +=1
            break
        elif answer1 not in answers:
            print("Please enter A, B, C, or D")
        else:
            print("Sorry, that is incorrect :(")
            print(f"Your score is {score} out of {question}")
            question +=1
            break

    answer2 = " "
    while answer2 not in answers:
        answer2 = input(f"Question: {question}\nWhat was the first commercially successful video game?\nA: Frogger\nB: Pong\nC: Joust\nD: The Sims\n").upper()

        if answer2 == "B":
            print("Correct!")
            score +=1
            print(f"Your score is {score} out of {question}")
            question +=1
            break
        elif answer2 not in answers:
            print("Please enter A, B, C, or D")
        else:
            print("Sorry, that is incorrect :(")
            print(f"Your score is {score} out of {question}")
            question +=1
            break

    answer3 = " "
    while answer3 not in answers:
        answer3 = input(f"Question: {question}\nWhat year was the Super Nintendo Entertainment System (SNES) released?\nA: 1991\nB: 2020\nC: 1980\nD: 1998\n").upper()

        if answer3 == "A":
            print("Correct!")
            score +=1
            print(f"Your score is {score} out of {question}")
            question +=1
            break
        elif answer3 not in answers:
            print("Please enter A, B, C, or D")
        else:
            print("Sorry, that is incorrect :(")
            print(f"Your score is {score} out of {question}")
            question +=1
            break
    



    break



