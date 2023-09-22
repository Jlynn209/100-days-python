from word_list import word_list
from ascii_art import stages
from ascii_art import logo
import random
import os


def game():

    chosen_word = random.choice(word_list)
    display = []
    letters_guessed = []
    lives = 6
    game_is_on = True


    for char in chosen_word:
        display.append("_")

    print(logo)

    while game_is_on:

        is_letter_found = False

        if "_" not in display:
            game_is_on = False
        
        if game_is_on == False:
            print("You win!")
            break

        while True:
            guess = input("Guess a letter: ").lower()
            os.system('cls')

            if guess in letters_guessed:
                print(f"You already guessed {guess}.")
                draw_display(display, lives)
            else:
                letters_guessed.append(guess)
                break

        for i in range(0, len(chosen_word)):

            if guess == chosen_word[i]:
                display[i] = guess
                is_letter_found = True
            
        if is_letter_found != True:
            print(f"{guess} is not in the word.")
            lives -= 1

        draw_display(display, lives)

        if lives == 0:
            game_is_on = False
            print(f"You lose, The word was {chosen_word}")
    
    restart_game()


def restart_game():
    do_restart = input("Do you want to play again?. Press Y for yes or N for no.").lower()

    if do_restart == "y":
        os.system('cls')
        game()
    else:
        print("Thanks for playing, Goodbye!")


def draw_display(display:list, lives:int):
    print(f"{' '.join(display)}")
    print(stages[lives])
