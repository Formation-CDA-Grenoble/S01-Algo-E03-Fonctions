def double(number):
    # Début de ton code
    if not type(number) is int:
        raise Exception("Argument must be an integer in double()")
    return number * 2
    # Fin de ton code



# Pas touche!
tests = (
    (2, 4),
    (7, 14),
    (0, 0),
    (-3, -6),
    ("pouet", 0),
)

for test in tests:
    print(f"L'appel  double({test[0]})  renvoie: {double(test[0])} (résultat attendu: {test[1]})")
