def main():
    c = int(input("Enter your remainder colombian pesos: "))
    b = int(input("Enter your remainder brazilian reais: "))
    p = int(input("Enter your remainder peruvian soles: "))

    mxn = round((c * 0.0054) + (b * 5.07) + (p * 3.28), 2)
    usd = round((mxn / 16.95), 2)

    print("USD:", usd)
    print("MXN:", mxn)

if __name__ == "__main__":
    main()
