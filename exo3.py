def isEqual(number1, number2):
    # Début de ton code
    return number1 == number2
    # Fin de ton code



# Pas touche!
tests = (
    (2, 2, True),
    (5, 12, False),
    (3, 3.0, True),
    ("bonjour", "bonjour", False),
)

for test in tests:
    print(f"L'appel  isEqual({test[0]}, {test[1]})  renvoie: {isEqual(test[0], test[1])} (résultat attendu: {test[2]})")
