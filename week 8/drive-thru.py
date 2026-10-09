def main():
    welcome()
    choice = int(input("select a number for your order: "))
    get_item(choice)

def welcome():
    lista = ["Cheeseburger", "Fries", "Soda", "Ice Cream", "Cookie"]

    print("Welcome to los pollos hermanos")
    print("select an item of the list")

    for item in range(len(lista)):
        print(f"{item + 1}. {lista[item]}")

def get_item(order):
    if order == 1:
        print("🍔")
    elif order == 2:
        print("🍟")
    elif order == 3:
        print("🥤")
    elif order == 4:
        print("🍦")
    elif order == 5:
        print("🍪")
    # kitchen = ["🍔", "🍟", "🥤", "🍦", "🍪"]
    # if 1 <= order <= 5:
    #     print(kithen[order - 1])
    else:
        print("dang bro use a number")




if __name__ == "__main__":
    main()
