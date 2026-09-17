def main():


    tasks = []

    while True:
        print(f"you have {len(tasks)} tasks to do")
        print(tasks)
        command = input("What do you whant to do? (add, complete, complete all, or end): ")
        if command == "add":
            new_task = input("add a task to the list: ")
            tasks.append(new_task)
        elif command == "complete":
            new_task = input("what task do you want to remove? ")
            tasks.remove(new_task)
            print(tasks)
        elif command == "complete all":
            tasks.clear()
            print(tasks)

        else:
            break




if __name__ == "__main__":
    main()
