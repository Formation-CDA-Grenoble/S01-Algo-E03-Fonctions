def reducer(list):
    # Début de ton code
    sum = 0
    for number in list:
        sum = sum + number
    return sum
    # Fin de ton code



# Pas touche!
tests = (
    ([1, 2, 3], 6),
    ([10], 10),
    ([1, 1, 1, 1, 1], 5),
    ([-12, 0, 50], 38),
)

for test in tests:
    print(f"L'appel  reducer({test[0]})  renvoie: {reducer(test[0])} (résultat attendu: {test[1]})")
