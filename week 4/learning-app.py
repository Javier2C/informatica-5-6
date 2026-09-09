import random

def main():

    print("Duo maths")

    streak = 0

    while streak < 3:

        number1 = random.randint(10, 99)
        number2 = random.randint(10, 99)

        answer = number1 + number2

        print(f"What is {number1} + {number2}?")

        user_answer = int(input("your answer: "))

        if user_answer == answer:
            print("Correct!")

            streak += 1

            print(f"Streak: {'⭐' * streak}")

        else:
            print("Incorrect.")
            print(f"The answer was {answer}")
            streak = 0

        print()

    print("Congratulations you got 3 correct in a row!")


if __name__ == "__main__":
    main()
