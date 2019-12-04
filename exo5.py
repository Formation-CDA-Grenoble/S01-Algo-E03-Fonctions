def cascadeMultiply(list, number):
    # Début de ton code
    pass
    # Fin de ton code



# Pas touche!
tests = (
    ([1, 2, 3], 2, [2, 4, 6]),
    ([1, 2, 3], -1, [-1, -2, -3]),
    ([-12, 0, 50], 10, [-120, 0, 500]),
    ([1, 1, 1], 0, [0, 0, 0]),
)

for test in tests:
    print(f"L'appel  cascadeMultiply({test[0]}, {test[1]})  renvoie: {cascadeMultiply(test[0], test[1])} (résultat attendu: {test[2]})")
