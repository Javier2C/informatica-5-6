def main():
    lista = [0]
    print("Welcome to the binary page")
    print("This program passes the code binary to write a whole number")

    while True:
        try:
            question = int(input("let´s put a binary code to make a whole number: "))
            if question == "1" and question == "0":
                for number in question:
                    print(number)
            else:
                print("just 1 and 0")

        except ValueError:
            print("invalid code")



def binary_to_decimal(binary):
    for binary in question:
        print(binary + (1*2))








if __name__ == "__main__":
    main()
