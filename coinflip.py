import random

def main():

    attempt = input(print("choose, heads or tails")).strip().lower()

    coin = random.randint(1, 2)
    print(coin)


    if coin == 1:
        result = "heads"

    else:
        result = "tails"

    print(result)

    if attempt == result:
        print("you win")

    else:
        print("you loose")


if __name__ == "__main__":
    main()
