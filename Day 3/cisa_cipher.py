alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'k', 'l']

direction = input("type encode to encrypt, type decode to decrypt : ")

message = input("type your message : ").lower()

shift = int(input("type the sgift number : "))


def cipher(direct, text_amount, shift_number):

    cipher_code = ""
    if direct == "decode" :
            shift_number *= -1   #shift_number = shift_number *  2 x -1 = -2
    for letter in text_amount:     
        postion = alphabets.index(letter) # h = 7 + -2
        new_position = postion + shift_number # -5
        cipher_code += alphabets[new_position] # 5
    print(f'the {direct}d is {cipher_code}')


cipher(direct=direction, text_amount=message ,shift_number=shift)


