name = input("What is your name? ").strip().title()
color = input("Tell me a color: ").strip().title()
adjective = input("Give me an adjective: ").strip().title()
goal = input("A goal you would like to achieve: ").strip().title()
print()


print(f"Hello, {name}!")
print()
print("This is your story:")

story = f"At dawn the sky turned {color}, and the air felt {adjective}. I decided today I will finally {goal}."

print(story)
print()
print("Yelling version:")
print(story.upper())
