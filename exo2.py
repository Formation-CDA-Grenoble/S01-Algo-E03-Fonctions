def conditionalDouble(number):
    # Début de ton code
    if not type(number) is int:
        raise Exception("Argument must be an integer in double()")
    return (number * 2) if number > 0 else number
    # Fin de ton code



# Pas touche!
tests = (
    (2, 4),
    (7, 14),
    (0, 0),
    (-3, -3),
)

for test in tests:
    print(f"L'appel  conditionalDouble({test[0]})  renvoie: {conditionalDouble(test[0])} (résultat attendu: {test[1]})")
