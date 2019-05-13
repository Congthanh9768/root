import random
alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '      
key = 'nu.t!iyvxqfl,bcjrodhkaew spzgm'
ans=True

while ans:
    print ("""
    1. Shift cipher
    2. Substitution cipher
    3. Euclide mở rộng
    4. Exit/Quit
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
        print("\n shift cipher")
        def shift(offset):
            message = input("Input Message You Would Like Encrypted:\n")
            new_message = ''

            for letter in message:

                letter = letter.lower() #doesn't handle upper-case yet

                if letter.isalpha():
                    shift_pos = alphabet.index(letter) + offset
                    new_pos = alphabet[shift_pos]
                    new_message += new_pos
                elif ' ' or '/t' or '/n' in letter: 
                    new_message += letter

                elif letter.isnumeric(): 
                    new_message += letter

                else:
                    print("An error took place in recording the message. Check input.\n")

            print(new_message)
        shift(-1)

    elif ans=="2":
        print("\n Substitution cipher") 
        plaintext = input("nhap message: ")

        def makeKey(alphabet):
           alphabet = list(alphabet)
           random.shuffle(alphabet)
           return ''.join(alphabet)

        def encrypt(plaintext, key, alphabet):
            keyIndices = [alphabet.index(k.lower()) for k in plaintext]
            return ''.join(key[keyIndex] for keyIndex in keyIndices)

        def decrypt(cipher, key, alphabet):
            keyIndices = [key.index(k) for k in cipher]
            return ''.join(alphabet[keyIndex] for keyIndex in keyIndices)

        cipher = encrypt(plaintext, key, alphabet)

        print(plaintext)
        print(cipher)
        print(decrypt(cipher, key, alphabet))
        #keyIndices = [alphabet.index(k.lower()) for k in plant]

    elif ans=="3":
      print("\n Euclide ở rộng")
      plaintext = input("nhap message: ")
      
    elif ans=="4":
      print("\n Goodbye") 
    elif ans !="":
      print("\n Not Valid Choice Try again")
