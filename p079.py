# 04/08/20

file = open('p079_keylog.txt')
codes = file.readlines()

codes = [code[:3] for code in codes]

freq_codes = {code:0 for code in codes}

digits_used = set()

for code in codes:
    digits_used = digits_used.union(set(code))
    freq_codes[code] += 1

super_dict = {digit:set() for digit in digits_used}


for code in codes:
    for digit in code[1:]:
        prev_index = code.index(digit)-1
        super_dict[digit].add(code[prev_index])

# print(codes)
# print(digits_used)
print(super_dict)

# 73162890
# βοήθεια γιατί δεν κατάλαβα εκφώνηση
# {'6': {'0', '9', '7', '3', '1'}, '8': {'6', '2', '0', '3', '1'}, '9': {'6', '2', '8', '7', '1'}, '0': {'6', '8', '9', '2', '1'}, '2': {'6', '0', '9', '7', '1'}, '7': {'6', '0', '2', '9', '8', '1'}, '3': {'6', '8', '9', '2', '0', '7'}, '1': {'8', '0', '9', '2', '7', '3'}}