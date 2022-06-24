message_file = open('p059_cipher.txt','r')
message = message_file.read().split(',')
message = list(map(int,message))
message_length = len(message) # 1455

words_file = open('p059_common_words.txt', 'r')
words_list = words_file.read().split('\n')

forbidden = set('@#$%^&*{}')
letters = list(range(97, 123))

def decryption(code_tuple): return chr(code_tuple[0]^code_tuple[1])

def main():

    possible_keys = [[i, j, k] for i in letters for j in letters for k in letters]

    for key in possible_keys:
        key_list = 485*key # Η λίστα με το κλειδί επαναλαμβανόμενο

        decr_list = list(map(lambda x: chr(x[0]^x[1]), zip(message, key_list))) # wow
        decrypted_message = ''.join(decr_list)

        if set(decrypted_message).intersection(forbidden) == set():
            print(sum(list(map(ord, decr_list))))
            return [decrypted_message, key]



if __name__ == '__main__':
    decr_message, key = main()
    key = ''.join(list(map(chr,key)))
