alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890! #@&*^+'
key = ''
scrambled_message = ''
secretalphabet = ''
newMessage = ''

def prompt_decrypt():
  print("\n ******** SUPER SECRET SPY SYSTEM  *********\n")
  print("super secret spy system is watching you now ...")
  print("you can decrypt your message now")
  global scrambled_message
  scrambled_message = input('Please enter the scrambled message: ')
  key = input('Enter your key (1-70): ')
  key = int(key)
  print("\n")
  return key

def decrypt(message, key):
  global newMessage
  print("decrypting ... ... ... ... ... done!")
  for character in message:
    if character in alphabet:
      position = alphabet.find(character)
      newPosition = (position - key) % 70
      newCharacter = alphabet[newPosition]
      newMessage += newCharacter
    else:
      newMessage += character
  

#the main program logic starts below
  
key = prompt_decrypt()
decrypt(scrambled_message, key)
print('Your decrypted message is: ', newMessage)
