import random

def Willkommen():
    print('''
Willkommen! Viel Spaß beim rechnen.
-Sofie Preißinger
''')


def Ratespiel():
    secretNumber = random.randint(1, 20)
    print('Erraten Sie eine Zahl zwischen 1 und 20 mit maximal 5 Versuchen')

    for guessesTaken in range (1,6):
        print('Erraten Sie die Zahl')
        guess = int(input())

        if guess < secretNumber:
            print(f'Die Zahl is höher als {guess} !')
        elif guess > secretNumber:
         print(f'Die Zahl ist kleiner als {guess} !')
        else:
            break

    if guess == secretNumber:
        if str(guessesTaken) : 1
        print('Gut gemacht! Sie haben ' + str(guessesTaken) + ' mal geraten')
    else:
        print('Die zufällige Nummer war ' + str(secretNumber))

    nochmal()

def nochmal():

    nochmalspielen = input('''
Wollen Sie es nochmal versuchen ?
Bitte geben Sie bitte "Ja" oder "Nein" ein.
''')

    if nochmalspielen == 'Ja':
        Ratespiel()

    elif nochmalspielen == 'Nein':
        print ('Spiel beendet.')

    else:
        nochmal()

Willkommen()
Ratespiel()
