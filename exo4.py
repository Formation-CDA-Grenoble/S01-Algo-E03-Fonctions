def cascadeDouble(number):
    # Début de ton code
    pass
    # Fin de ton code



# Pas touche!
tests = (
    ([1, 2, 3], [4, 5, 6]),
    ([10], [20]),
    ([1, 1, 1, 1, 1], [2, 2, 2, 2, 2]),
    ([-12, 0, 50], [-24, 0, 100]),
)

for test in tests:
    print(f"L'appel  cascadeDouble({test[0]})  renvoie: {cascadeDouble(test[0])} (résultat attendu: {test[1]})")
