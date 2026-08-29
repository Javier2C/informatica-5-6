def main():

    print("Chum Bucket")
    rating = float(input("Rating given from 0-5"))

    if rating > 4.5:
        print("Perfection")
    elif rating > 4:
        print("Excellent")
    elif rating > 3:
        print("Good")
    elif rating > 2:
        print("Fair")
    else:
        print("Disgusting")

    print("come back")






if __name__ == "__main__":
    main()

