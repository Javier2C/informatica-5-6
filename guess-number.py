import random

def main():

    name = input(print("what is your name?"))
    print(name)

    number = ""
    number = random.randint(1, 100)
    guess = int(input("Guess the number from 1 to 100"))



    while guess != number:
        if guess > number:
            print("higher")
        elif guess < number:
            print("lower")
        else guess == number:
            break






if __name__ == "__main__":
    main()
