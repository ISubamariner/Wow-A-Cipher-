
def encryption_state():#Choice of Encryption or Decryption loop
    counter=0
    while True:
        counter += 1
        if counter > 10:
            print('Too many invalid inputs')
            exit()
            
        action = input("\nAre you here to encrypt(Y/N)? ")
        
        if action.lower() == "y":
            return True
            
        elif action.lower() =="n":
            action= input("\nAre you here to decrypt(Y/N)? ")
            
            if action.lower() =="y":
                return False
        
        

def custom_key_checker():#Loops until key is valid
    counter=0
    while True:
        checker= True
        counter +=1
        if counter > 10:
            print('Too many invalid inputs')
            exit()
            
        custom_key = input('Input encryption key: ').lower()
        
        for i in custom_key:
            if not i.isalpha():
                checker= False
                
        if checker == False:
            print ("Key should be alphanumeric without punctuations and spaces.")
        
        elif checker == True:
            return custom_key
            

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message
    
def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)   

#Program Execution
action=encryption_state()
text = input('Enter the message: ')
custom_key= custom_key_checker()

if action == True:
    print (f'Original Message: {text}')
    print (f'Encrypted Message: {encrypt(text,custom_key)}')
    
elif action == False:
    print (f'Original Message: {text}')
    print (f'Decrypted Message: {decrypt(text,custom_key)}')
    
   

