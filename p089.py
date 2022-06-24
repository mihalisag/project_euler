import roman
from pprint import pprint

file = open('p089_roman.txt', 'r')
text = file.readlines()
text = [roman[:-1] for roman in text]
text[-1] = 'XXXXVIIII'

denominations = {'I': 1,
              'V': 5,
              'X': 10,
              'L': 50,
              'C': 100,
              'D': 500,
              'M': 1000,
}

def inv_rom_to_int(rom):

    num = 0

    for char in rom:
        num += denominations[char]
        
    return num

charac = 0
l = []

for rom in text:
    try:
        charac += len(rom) - len(roman.toRoman(roman.fromRoman(rom)))
    except roman.InvalidRomanNumeralError:
        l.append(rom)

print(l)
print(charac)


# charac = 0
# l = []

# for rom in text:

#     n = inv_rom_to_int(rom)

#     if n <= 4999:
#         charac += len(rom) - len(roman.toRoman(inv_rom_to_int(rom)))

# print(charac)

# 820
# [('MMMMCMLXXXXVIII', 5198),
#  ('MMMMCML', 5150),
#  ('MMMMCMLVI', 5156),
#  ('MMMMCMLXXXXV', 5195),
#  ('MMMMCMXV', 5115),
#  ('MMMMCMLII', 5152),
#  ('MMMMCMXLVIII', 5168),
#  ('MMMMCMLI', 5151),
#  ('MMMMCML', 5150),
#  ('MMMMCMXXXV', 5135),
#  ('MMMMDCCCCXCV', 5015),
#  ('MMMMCMLXII', 5162),
#  ('MMMMCMIV', 5106)]
