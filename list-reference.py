def main():

    objects = ["pencil", "computer", "chair", "paper", "yoyo", "nickel"]
    print(len(objects)) #me sirve para contar cuantas cosas hay en la lista

    objects.pop(0)
    print("lista con pop:", objects)

    objects.remove("paper")
    print("lista con remove:", objects)

    objects.sort()
    print(objects)

    objects.append("sofia")
    print(objects)







if __name__ == "__main__":
    main()
