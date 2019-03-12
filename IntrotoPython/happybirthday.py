'''  Using functions '''

def happyBirthday(person):
    #print("\n")
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear " + person + ".")
    print("Printing Me First Happy Birthday to you!")
    #print("\n")

def main():
    happyBirthday('Leela')
    happyBirthday('Nanditha')
    happyBirthday('Anika')

    userName = input("Enter the Birthday person's name: ")
    happyBirthday(userName)

    
main()
