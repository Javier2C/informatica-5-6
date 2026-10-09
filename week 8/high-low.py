def main():

    def highest(a, b):
        if a > b:
            highest_number = a
            lowest_number = b
            print(f"{a} is greater than {b}")

        elif b > a:
            highest_number = b
            lowest_number = a
            print(f"{b} is greater than {a}")

        # elif b < a:
        #     lowest_number = b
        #     print(f"{b} is less than {a}")

        # elif a > b:
        #     lowest_number = a
        #     print(f"{a} is less than {b}")

        else:
            print("the numbers are equal")
        print(f"the highest number is {highest_number}")
        print(f"the lowest number is {lowest_number}")
    highest(8, 2)

    num1 = float(input("put a number: "))
    num2 = float(input("put another number: "))

    highest(num1, num2)





if __name__ == "__main__":
    main()
