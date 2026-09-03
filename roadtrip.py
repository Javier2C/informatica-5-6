def main():
    answer = "" #initialize
    followup = ""

    while answer != "Yes!": #condition
        answer = input("are we there yet").strip().title() #update
        if answer == "Yes":
            followup = input("really?").strip().title()
        if followup == "Yes!":
            break

    print("we just arrived")





if __name__ == "__main__":
    main()
