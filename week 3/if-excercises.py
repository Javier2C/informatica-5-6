def main():


    one = float(input(print("First number:")))
    two = float(input(print("Second number:")))
    three = input(print("Put the sign operation"))

    if three == "+":
        plus = one + two
        print(plus)

    elif three == "-":
        minus = one - two
        print(minus)

    elif three == "*":
        times = one * two
        print(times)

    elif three == "/":
        divide = one / two
        print(divide)

    else:
        print("")






if __name__ == "__main__":
    main()
