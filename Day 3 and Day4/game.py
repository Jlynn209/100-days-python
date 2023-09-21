import ascii
import random
import time
import os
import json


def game():

    is_playing = True

    while is_playing:

        # Read match data
        with open("data.json", "r") as json_file:
            data = json.load(json_file)
        
        print(f"Wins: {data['wins']}, Losses: {data['losses']}")

        # Loop until a valid choice is given for user input
        while True:

            try: 
                user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

                if user_choice <= 2:
                    break
                else:
                    invalid_error_message()
            except ValueError:
                invalid_error_message()
            
        # Draw user image 
        print(ascii.choices[user_choice])

        time.sleep(1)
        print("Computer chose:")
        time.sleep(1)

        computer_choice = random.randint(0,2)
        # Draw Computer Image
        print(ascii.choices[computer_choice])

        winning_outcomes = {
            # Player:Computer
            0:2,
            1:0,
            2:1,
        }

        if user_choice == computer_choice:
            print("You tied")
        elif winning_outcomes[user_choice] == computer_choice:
            data["wins"] += 1
            print("You Win!")
        else:
            data["losses"] += 1
            print("You Lose!")

        # Save match data
        with open("data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        if restart_option() == False:
            is_playing = False
        else:
            os.system('cls')
    
    print("Goodbye!")
    time.sleep(2)
    os.system('cls')


def invalid_error_message():
    print("Please choose a valid option")
    time.sleep(2)
    os.system('cls')


def restart_option():

    restart_option = input("\nDo you want to play again? press Y for Yes or N for No: ")
    if restart_option.upper() == "Y":
        return True
    
    return False