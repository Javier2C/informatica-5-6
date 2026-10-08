def main():
    print("Welcome to the binary page")
    print("This program passes the code binary to write a whole number")

    
    try:
        question = input(int("let´s put a binary code to make a whole number: "))
        for number in question:
            print(number)

    except ValueError:
        print("enter a number")



#def binary_to_decimal():









if __name__ == "__main__":
    main()
