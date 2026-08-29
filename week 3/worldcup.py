def main():
    spain = int(input("Spain goals: "))
    argentina = int(input("Argentina goals: "))

    if spain > argentina:
        print("Spain is the winner")
    elif argentina > spain:
            print("Argentina is the winner")
    else:
         print("TIE")

    print("Congrats")



if __name__ == "__main__":
    main()

