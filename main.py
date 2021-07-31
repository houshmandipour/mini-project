import random
import time


def welcome():
    print("* * * Welcome to Hangman game * * *  \n")
    time.sleep(1)
    print(" Loading ")
    time.sleep(2)

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    global result
    words_to_guess = ["ant", "summer", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage",
                      "dog", "sunny", "imagine", "kamel"]
    word = random.choice(words_to_guess)
    result = word
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""


def play_loop():
    global play_game
    # play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y" or "Y":
        main()
    if play_game == "n" or "N":
        print("Thanks For Playing! We expect you back again!")
        exit()


def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " + display + "\n Enter your guess:  ")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    elif guess in already_guessed:
        print("Try another letter.\n")
    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print("Wrong guess. " + str(limit - count) + " guesses remaining   |#|_|_|_|_|\n")
        elif count == 2:
            time.sleep(1)
            print("Wrong guess. " + str(limit - count) + " guesses remaining   |#|#|_|_|_|\n")
        elif count == 3:
           time.sleep(1)
           print("Wrong guess. " + str(limit - count) + " guesses remaining   |#|#|#|_|_|\n")
        elif count == 4:
            time.sleep(1)
            print("Wrong guess. " + str(limit - count) + " last guess remaining   |#|#|#|#|_|\n")
        elif count == 5:
            time.sleep(1)
            print("Wrong guess. You are hanged!!!   |#|#|#|#|#|\n")
            print()
            print("The word was:", result)
            play_loop()
    if word == '_' * length:
        print("*"*10)
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


if __name__ == "__main__":
    welcome()
    main()
    hangman()

