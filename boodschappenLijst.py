import os.path

# Controleert eerst of het gevraagde bestand bestaat. Als het bestaat, voegt het regels toe aan de array

path = './boodschappenLijst.txt'

check_file = os.path.isfile(path)

array = []

if check_file:
    with open('boodschappenLijst.txt') as f:
        for line in f:
            array.append(line[:-1])
        print(array)




# Functie om te controleren of er al een waarde in de array aanwezig is
def is_duplicate(array, value):
    return value in array

# Krijg input van de gebruiker en sla unieke waarden op in een array en een tekstbestand

while True:
    user_input = input("Voer een waarde in (of 'q' om te stoppen): ")

    if user_input == 'q':
        break
    if not is_duplicate(array, user_input):
        array.append(user_input)
        file = open("boodschappenLijst.txt", "a")
        file.writelines( user_input + "\n")
        print(f"{user_input} is added to list.")
        
        file.close()

    elif is_duplicate(array,user_input):
        
        print(f"{user_input} is already added to list.")
    
        


