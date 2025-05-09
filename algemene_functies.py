def mijn_functie_1(lijst1):
 return [x ** 2 for x in lijst1]

lijst1 = [2, 4, 10, 12]
print(mijn_functie_1(lijst1))


def mijn_functie_2(lijst2):
 return [(a + b, a - b, a * b, int(a / b)) for a, b in lijst2]

lijst2 = [(12, 3), (12, 2), (10, 5), (100, 20)]
print(mijn_functie_2(lijst2))