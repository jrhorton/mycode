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
            print(f"Your score is {score} out of {question}\n")
            question +=1
            break
        elif answer1 not in answers:
            print("Please enter A, B, C, or D")
        else:
            print("Sorry, that is incorrect :(")
            print(f"Your score is {score} out of {question}\n")
            question +=1
            break

    answer2 = " "
    while answer2 not in answers:
        answer2 = input(f"Question: {question}\nWhat was the first commercially successful video game?\nA: Frogger\nB: Pong\nC: Joust\nD: The Sims\n").upper()

        if answer2 == "B":
            print("Correct!")
            score +=1
            print(f"Your score is {score} out of {question}\n")
            question +=1
            break
        elif answer2 not in answers:
            print("Please enter A, B, C, or D")
        else:
            print("Sorry, that is incorrect :(")
            print(f"Your score is {score} out of {question}\n")
            question +=1
            break

    answer3 = " "
    while answer3 not in answers:
        answer3 = input(f"Question: {question}\nWhat year was the Super Nintendo Entertainment System (SNES) released?\nA: 1991\nB: 1989\nC: 1984\nD: 1998\n").upper()

        if answer3 == "A":
            print("Correct!")
            score +=1
            print(f"Your score is {score} out of {question}\n")
            question +=1
            break
        elif answer3 not in answers:
            print("Please enter A, B, C, or D")
        else:
            print("Sorry, that is incorrect :(")
            print(f"Your score is {score} out of {question}\n")
            question +=1
            break
    
    answer4 = " "
    while answer4 not in answers:
        answer4 = input(f"Question: {question}\nWhat food was the character Pac Man modeled after?\nA: A potato\nB: Calzone\nC: Cheeseburger\nD: Pizza\n").upper()
          
        if answer4 == "D":
            print("Correct!")
            score +=1
            print(f"Your score is {score} out of {question}\n")
            question +=1
            break
        elif answer4 not in answers:
            print("Please enter A, B, C, or D")
        else:
            print("Sorry, that is incorrect :(") 
            print(f"Your score is {score} out of {question}\n")
            question +=1 
            break
    
    answer5 = " "
    while answer5 not in answers:
        answer5 = input(f"Question: {question}\nWhat is the highest-selling gaming console to date?\nA: NES\nB: PS2\nC: XBox One\nD: PS4\n").upper()

        if answer5 == "B":
            print("Correct!")
            score +=1
            print(f"Your score is {score} out of {question}\n")
            question +=1
            break
        elif answer5 not in answers:
            print("Please enter A, B, C, or D")
        else:
            print("Sorry, that is incorrect :(")
            print(f"Your score is {score} out of {question}\n")
            question +=1
            break

    answer6 = " "
    while answer6 not in answers:
        answer6 = input(f"Question: {question}\nWhat year was Nintendo founded?\nA: 1989\nB: 1992\nC: 1985\nD: 1990\n").upper()

        if answer6 == "A":
            print("Correct!")
            score +=1
            print(f"Your score is {score} out of {question}\n")
            question +=1
            break
        elif answer6 not in answers:
            print("Please enter A, B, C, or D")
        else:
            print("Sorry, that is incorrect :(")
            print(f"Your score is {score} out of {question}\n")
            question +=1
            break
        
    answer7 = " "
    while answer7 not in answers:
        answer7 = input(f"Question: {question}\nBlizzard Entertainment is most well known for what video game franchise??\nA: Overwatch\nB: World of Warcraft\nC: Diablo\nD: Starcraft\n").upper()

        if answer7 == "B":
            print("Correct!")
            score +=1
            print(f"Your score is {score} out of {question}\n")
            question +=1
            break
        elif answer7 not in answers:
            print("Please enter A, B, C, or D")
        else:
            print("Sorry, that is incorrect :(")
            print(f"Your score is {score} out of {question}\n")
            question +=1
            break
        
    answer8 = " "
    while answer8 not in answers:
        answer8 = input(f"Question: {question}\nWhat video game company collaborated with SONY on the Playstation?\nA: Sega\nB: NEO GEO\nC: Microsoft\nD: Nintendo\n").upper()

        if answer8 == "D":
            print("Correct!")
            score +=1
            print(f"Your score is {score} out of {question}\n")
            question +=1
            break
        elif answer8 not in answers:
            print("Please enter A, B, C, or D")
        else:
            print("Sorry, that is incorrect :(")
            print(f"Your score is {score} out of {question}\n")
            question +=1
            break
        
    answer9 = " "
    while answer9 not in answers:
        answer9 = input(f"Question: {question}\nThe United States Air Force used what gaming console to create a cluster supercomputer?\nA: Gamecube\nB: PS3\nC: XBox 360\nD: Sega Genesis\n").upper()

        if answer9 == "B":
            print("Correct!")
            score +=1
            print(f"Your score is {score} out of {question}\n")
            question +=1
            break
        elif answer9 not in answers:
            print("Please enter A, B, C, or D")
        else:
            print("Sorry, that is incorrect :(")
            print(f"Your score is {score} out of {question}\n")
            question +=1
            break
        
    answer10 = " "
    while answer10 not in answers:
        answer10 = input(f"Question: {question}\nHow much did a virtual reality device cost in 1980?\nA: $49,000\nB: $123,000\nC: $12,500\nD: Tree fiddy\n").upper()

        if answer10 == "A":
            print("Correct!")
            score +=1
            print(f"Your score is {score} out of {question}\n")
            question +=1
            break
        elif answer10 not in answers:
            print("Please enter A, B, C, or D")
        else:
            print("Sorry, that is incorrect :(")
            print(f"Your score is {score} out of {question}\n")
            question +=1
            break

    if score == 10:
        print("You scored 10 out of 10... you are a god amoungst men. Bask in the glory of your intellectual triumph!")
    elif score >= 8:
        print(f"Awesome!!! You scored {score} out of 10. You are truely a video game connoisseur for the ages.")
    elif score >= 6:
        print(f"Pretty good job getting {score} out of 10. You've obviously played some games over the years.")
    elif score >= 4:
        print(f"Well.. you scored {score} out of 10. Not terrible, but definitely not a ""GG"".")
    elif score >= 2:
        print(f"Seriously?!?! {score} out of 10? That's it? Go back to Hello Kitty Online, noob")
    else:
        print(f"{score} out of 10... You are potato.")

    print("Thanks for playing!")

    break



