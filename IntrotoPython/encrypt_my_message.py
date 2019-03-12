alphabet = 'abcdefghijklmnopqrstuvwxyz'
secretalphabet = ''
newMessage = ''

def prompt():
  print("\n ******** SUPER SECRET SPY SYSTEM  *********\n")
  print("super secret spy system is watching you now ...")
  print("you can encrypt your message now")

def secretalpha(key):
  secretalphabet = ''
  for character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    secretcharacter = alphabet[newPosition]
    secretalphabet = secretalphabet + secretcharacter
  print(secretalphabet)

prompt()
message = input('Please enter a message: ')
key = input('Enter a key (1-26): ')
key = int(key)
print("\n")
print(alphabet)
secretalpha(key)
print("\n")

for character in message:
    if character in alphabet:
      position = alphabet.find(character)
      newPosition = (position + key) % 26
      newCharacter = alphabet[newPosition]
      newMessage = newMessage + newCharacter
    else:
      newMessage = newMessage + character
print('Your new excrypted message is: ', newMessage)

