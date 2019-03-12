#dictionary of animals and sounds
'''
bats            screech
Crows	        caw
Dolphins	click
Eagles	        scream
Elephants	trumpet
Kangaroos	chortle
Pigeons	        coo
Nightingales	sing

'eagles':'scream',
                'elephants':'trumpet',
                'kangaroos':'chortle',
                'pigeons':'coo',
                'nightingales':'sing'}

'''

animalsounds = {'bats':'screech',
                'crows':'caw',
                'dolphins':'click'}
                
print(animalsounds.keys())
animal = input("Enter any animal (plural) from the table above:\n")

print("You entered: " + animal)

sound = "not found"
sound = animalsounds[animal]

print(animal + "  " + sound)

print("List of all sounds in this dictionary: ")
print(animalsounds.values())

      

