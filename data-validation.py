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

    while True:
        try:

            name = input("enter your name: ")
            f_letter = name[0]
            print("name stored successfully")
            break

        except IndexError:
            print("please enter your name -_-")








if __name__ == "__main__":
    main()
