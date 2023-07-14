
import random

def Willkommen():
    print('''
Willkommen! Viel Spaß beim rechnen.
-Sofie Preißinger
''')


def Ratespiel():
    secretNumber = random.randint(1, 20)
    print('Erraten Sie eine Zahl zwischen 1 und 20 mit maximal 5 Versuchen')

    guess = None

    for guessesTaken in range (1, 6):
        print('Erraten Sie die Zahl')
        try:
            guess = int(input())

        except ValueError:
            print ('Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 1 und 20 ein.')

            continue

        if guess < secretNumber:
            print(f'Die Zahl is höher als {guess} !')
        elif guess > secretNumber:
         print(f'Die Zahl ist kleiner als {guess} !')
        else:
            break

    if guess == secretNumber:
        print('Gut gemacht! Sie haben ' + str(guessesTaken) + ' mal geraten')
    else:
        print('Die zufällige Nummer war ' + str(secretNumber))

    nochmal()

def nochmal():
    while True:
        nochmalspielen = input('''
Wollen Sie es nochmal versuchen ?
Bitte geben Sie "Ja" oder "Nein" ein.
''')

        if nochmalspielen.lower() == 'ja':
            Ratespiel()
            break

        elif nochmalspielen.lower() == 'nein':
            print ('Spiel beendet.')
            break

        else:
            print('Ungültige Eingabe. Bitte geben sie "Ja" oder "Nein" ein.')

Willkommen()
Ratespiel()
