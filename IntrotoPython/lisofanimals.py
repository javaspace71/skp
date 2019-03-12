#list of animals and sounds
'''
bats            screech
Crows	        caw
Dolphins	click
Eagles	        scream
Elephants	trumpet
Kangaroos	chortle
Pigeons	        coo
Nightingales	sing
'''

animals = ['bats', 'crows', 'dolphins', 'eagles', 'elephants', 'kangaroos', 'pigeons', 'nightingales']
sounds  = ['screech', 'caw', 'click', 'scream', 'trumpet', 'chortle', 'coo', 'sing']

print(animals)
animal = input("Enter any animal (plural) from the list above:\n")

print("You entered: " + animal)

position = animals.index(animal)

#sound = "not found"
sound = sounds[position]

print(animal + " " + sound)

