from fractions import Fraction

proper_list = []

for num in range(1, 10**3):
    for den in range(1, 10**3):
        proper_list.append(Fraction(num, den))

proper_list.sort()

print(proper_list[proper_list.index(Fraction(3, 7))-1])


# ΟΧΙ ΕΤΣΙ ΤΟ ΕΚΑΝΑ ΣΤΟ ΧΑΡΤΙ