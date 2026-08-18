def main():
    c_money = int(input("Enter your remainder colombian pesos: "))
    b_money = int(input("Enter your remainder brazilian reais: "))
    p_money = int(input("Enter your remainder peruvian soles: "))

    usd = ((c_money / 3111.24) + (b_money / 0.19) + (p_money / 0.30))
    print("USD:", usd)

    mxn = (usd / 17.06)
    print(round("MXN:", mxn), )

if __name__ == "__main__":
    main()
