def cascadeIsPositive(list):
    # Début de ton code
    result = []
    for number in list:
        # Si le nombre est égal à zéro
        if number == 0:
            # Ajoute None dans la liste
            result.append(None)
        # Sinon
        else:
            # Ajoute dans la liste True ou False en fonction du signe du nombre
            result.append(number > 0)
    return result
    # Fin de ton code



# Pas touche!
tests = (
    ([1, 2, 3], [True, True, True]),
    ([10], [True]),
    ([1, -1, 1, -1, 1], [True, False, True, False, True]),
    ([-12, 0, 50], [False, None, True]),
)

for test in tests:
    print(f"L'appel  cascadeIsPositive({test[0]})  renvoie: {cascadeIsPositive(test[0])} (résultat attendu: {test[1]})")
