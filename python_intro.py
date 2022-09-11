print("Ahoj, Django Girls!")
if 3 > 2:
    print("Funguje to!")
if 5 > 2:
    print("5 je naozaj viac ako 2")
else:
    print("5 nie je viac ako 2")

meno = "Sona"
if meno == "Yuliya":
    print("Cao Yuliya!")
elif meno == "Sona" :
    print("Cao Sona!")
else:
    print("Cao neznama!")

volume = 57
if volume < 20:
    print ("Je to pomerne tiche.")
elif 20 <= volume < 40:
    print("Je to fajn ako hudba na pozadi")
elif 40 <= volume < 60:
    print("Super,pocujem vsetky detaily")
else:
    print("Bolia ma usi! :(")

#Zmen hlasitost, ak je prilis silna alebo slaba
if volume < 20 or volume > 80:
    volume = 50
    print("Lepsie!")

def ahoj():
    print('Ahoj!')
    print('Ako sa mas?')

ahoj()

def ahoj(meno):
    if meno == 'Yuliya':
        print('Ahoj Yuliya!')
    elif meno == 'Sona':
        print('Ahoj Sona!')
    else:
        print('Ahoj neznama!')

ahoj("Anna")

def ahoj(meno):
    print('Ahoj ' + meno + '!')

ahoj("Kika")

dievcata = ['Katka', 'Kika', 'Zuza', 'Ola', 'Yuliya']

for meno in dievcata:
    ahoj(meno)
    print('Dalsie dievca')

for i in range(1, 6):
    print(i)
    
