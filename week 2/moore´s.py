def main():
    transistors = 17000000000
    years = int(input("how many years?"))
    transistors = transistors * 2 **(years / 2)
    print("transistors left:", transistors)

if __name__ == "__main__":
    main()
