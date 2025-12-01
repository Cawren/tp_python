string = input("Saisissez une chaîne : ")
n_letters = 0
n_numbers = 0
for char in string :
    if char.isalpha() :
        n_letters += 1
    elif char.isnumeric() :
        n_numbers += 1
print (f"Lettres : {n_letters}\nChiffres : {n_numbers}")