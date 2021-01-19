alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'k', 'l']

direction = input("type encode to encrypt, type decode to decrypt : ")

message = input("type your message : ").lower()

shift = int(input("type the sgift number : "))

def ceafar(direct, msg, shift_number) :

  cipher_code = ""
  for letter in msg :
    postion  = alphabets.index(letter)
    if direct == 'encode':
      new_position = postion + shift_number
    elif direct == 'decode':
      new_postion = postion - shift_number
    cipher_to_word = alphabets[new_position]
    cipher_code += cipher_to_word 
    
  print(f"your code is ; {cipher_code}")

ceafar(direct=direction, msg=message, shift_number=shift)
 
    
    
    
    
    
      