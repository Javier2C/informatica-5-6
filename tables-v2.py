def main():

    print("Times Table QUIZ")
    times_table = int(input("Enter a times table that you would like to be tested on (1-10): "))

    max_value = int(input("enter the max value for your quiz: "))

    if 1 <= times_table <= 10:

        print(f"Here is the {times_table} times table")

        for x in range(max_value):
                answer = x * times_table
                
                print(f"you will be tested on your chosen times table")

    else:
            print("Invalid command.")







if __name__ == "__main__":
    main()
