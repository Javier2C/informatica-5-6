def main():
    width = int(input("Enter the width of the rectangle: "))
    print( "O" * width)
    print( "O" * width)
    print( "O" * width)
    print( "O" * width)
    print( "O" * width)

    p = (5 * 2) + (width * 2)
    print("perimeter:", p)

if __name__ == "__main__":
    main()
