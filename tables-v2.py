def main():

    print("Times Table QUIZ")
    times_table = int(input("Enter a times table that you would like to be tested on (1-10): "))



    if 1 <= times_table <= 10:

        print(f"Here is the quiz for {times_table} times table")

        for x in range(1, max_value):
                answer = x * times_table
                print(f"how much is {times_table} * {x}:" )
                user_answer = int(input("your answer: "))

    



    else:
            print("Invalid command.")







if __name__ == "__main__":
    main()
