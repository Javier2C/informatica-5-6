def main():

    not_validated = True
    while not_validated:

        try:

            number = int(input("Enter a number between 1-10: "))
            if number >= 1 and number <= 10:
                print("Number stored successfully")
                not_validated = False
            else:
                print("enter a number from 1-10!!!!!!")



        except ValueError:
            print("ENTER A NUMBER. 🤬🤬🤬🤬🤬🤬🤬🤬")









if __name__ == "__main__":
    main()
