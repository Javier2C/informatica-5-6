import random

def main():

    name = input(print("what is your name?"))
    print(name)

    guess = 0
    number = random.randint(1, 100)
    guess = int(input("Guess the number from 1 to 100"))



    while guess != number:
        guess = int(input("take a guess:"))
        if guess > number:
            print("your guess is too high")
        elif guess < number:
            print("your guess is too low")
    print(f"good job{name}!")





if __name__ == "__main__":
    main()
