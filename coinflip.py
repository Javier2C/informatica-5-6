import random

def main():

    attempt = input(print("choose, heads or tails")).strip().lower()
    
    coin = random.randint(1, 2)
    print(coin)


    if coin == 1:
        print("heads")

    elif coin == 2:
        print("tails")

    elif attempt == coin:
        print("you win")

    else:
        print("you loose")


if __name__ == "__main__":
    main()
