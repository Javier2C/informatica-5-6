import random

def main():
    start_game("words.txt")


def start_game(file):
    attempts = 10
    with open(file) as f:
        word_bank = f.read().splitlines()
    word = random.choice(word_bank).lower()
    hint = ["_"] * len(word)
    incorrect_letters = []
    while attempts > 0:
        print("Current word:", " ".join(hint))

        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1:
                break

            else:
                print("Invalid guess. Try again.")

        if guess in word and guess not in hint:
            for i in range(len(word)):
                if word[i] == guess:
                    hint[i] = guess
            print("Great guess!")
        elif guess in hint:
            attempts -= 1
            print("You already guessed that letter! Attempts left:", str(attempts))

        else:
            attempts -= 1
            print("Wrong guess! Attempts left:", str(attempts))
            if guess not in incorrect_letters:
                incorrect_letters.append(guess)
            print(f"Incorrect letters: {" ".join(incorrect_letters)}")

        if "_" not in hint:
            print("Congratulations! 🥳 You guessed the word:", word)
            break

    if attempts == 0 and "_" in hint:
        print("No attempts left 💀 The word was:", word)




if __name__ == "__main__":
    main()


# create a TXT file with all of the words.
# Define the main function
# Present the game
# call start_game function
# use len to accomodate the function
# Use with to open the TXT file
# Define start_game(file)
# make a codeline to choose a random word from the TXT file
# make a variable for attempts
# make a variable list for the already chosen letters that were correct
# make a variable list for the already chosen letters that were incorrect
# make an if function for when the user puts a correct answer
# make an elif function for when the user puts a wrong answer
# make an elif function for when the user puts  answer
# make a input to ask the user for the letter
