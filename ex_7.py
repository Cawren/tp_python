numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

n_odd = 0
n_even = 0
for number in numbers :
    if number%2 == 0 :
        n_even += 1
    else :
        n_odd += 1

print(f"Nombre de nombres pairs : {n_even}\nNombre de nombres impairs : {n_odd}")