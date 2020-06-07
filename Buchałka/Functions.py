def python_food(*texts): # Parametr
    concatenated_value = " "
    for text in texts:
        concatenated_value += text + " "

    left_margin = (80 - len(concatenated_value)) // 2
    print(" " * left_margin, concatenated_value)


python_food("Mienso i jaja")# Argument
python_food("Mienso i jaja", "123")
