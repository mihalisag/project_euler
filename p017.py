words_to_19 = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen',
         'fifteen','sixteen','seventeen','eighteen','nineteen','']
words_tens = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

# d_19= {}

# for num in range(1,20):
#     d_19[num] = words_to_19[num-1]


tens = lambda n: words_tens[n//10 - 2] + '-' + words_to_19[n % 10 - 1]

def num_to_word(n):

    digits = len(str(n))

    if digits == 1:
        word = words_to_19[n-1]
    elif digits == 2:
        if n<=19:
            word = words_to_19[n-1]
        else:
            word = tens(n)
    elif digits == 3:
        word = ''

        if n%100 >= 1: word = ' and ' 
        word = words_to_19[n//100 - 1] + ' hundred' + word
        
        if (n%100)//10 > 1 : word = word + tens(n%100)
        elif n%100 == 10: word = word + 'ten'
        else: word = word + words_to_19[n%100 - 1]


    return word

letters = 0

for num in range(1,1000):
    
    word = num_to_word(num)
    if '-' in word: letters -= 1
    if ' ' in word: word = word.replace(' ','')
    

    letters += len(word)

print(letters+11) # 11 = number of digits of 1000