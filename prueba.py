def main():
    # 2. Mensaje de bienvenida modificado
    print("Welcome to the times table quiz")

    # 10. Validación para la tabla de multiplicar elegida
    while True:
        try:
            # 3. Input adaptado para el quiz (número entre 1 y 10)
            times_table = int(input("Enter a times table that you would like to be tested on (1-10): "))
            if 1 <= times_table <= 10:
                break
            else:
                print("Please enter a number strictly between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # 4 e 10. Validación para el valor máximo del quiz
    while True:
        try:
            max_value = int(input("Enter the maximum value for your times table: "))
            if max_value > 0:
                break
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # 4. Incrementar max_value en 1 para que el ciclo range() incluya este límite
    max_value += 1

    # 5. Frase modificada antes de iniciar el quiz
    print(f"\nHere is your quiz on the {times_table} times table")

    # Reto: Sistema de puntuación inicializado en 0
    score = 0
    total_questions = max_value - 1

    # 4. El ciclo ahora usa max_value para controlar el rango
    for x in range(1, max_value):
        correct_answer = x * times_table

        # 8. Código ajustado para ocultar la respuesta en la pregunta
        print(f"\n{x} times {times_table} is ...")

        # 6 e 10. Validación para la respuesta del usuario dentro del ciclo
        while True:
            try:
                user_answer = int(input("Answer: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric answer.")

        # 7. Condicional if-else para verificar la respuesta e incrementar el puntaje
        if user_answer == correct_answer:
            print("correct")
            score += 1
        else:
            print("incorrect")

    # Reto: Mostrar los resultados finales al terminar el quiz (Paso 9)
    print("\n--- Quiz Finished ---")
    print(f"Your final score is: {score} out of {total_questions}")


if __name__ == "__main__":
    main()
