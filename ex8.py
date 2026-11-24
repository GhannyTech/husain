import os
import random

doc = "puntuacions.csv"

salir = "4. Sortir"
punt = "2. Puntuació actual"
hist = "3. Historic de puntuacions"
partida = "1. Nova partida"

opciones = {"2": "📜", "3": "✂️", "1": "🪨"}

nom = ""
puntuaciojugador = 0
puntuaciopc = 0
historicjugador = 0


while True:

    os.system("cls")

    print(partida)
    print(punt)
    print(hist)
    print(salir)

    jugador = int(input("\nTria una de les opcions: "))

    os.system("cls")

    if jugador == 1:
        nom = input("Com et dius? ")
        os.system("cls")
        print(f"Benvingut {nom}!!\n")

        while True:
            print("Escull la teva tirada, ha de ser de les següents (escriu el numero): \n> Pedra🪨    (1) \n> Paper📜   (2) \n> Tisores✂️  (3)\n")
            jugador = input("Que vols tirar? ")
            os.system("cls")

            if jugador not in opciones:
                print("Opció no vàlida, torna a probar\n")
                continue

            ordinador = random.choice(list(opciones.keys()))

            print(f"Humanoide🧠: {opciones[jugador]}")
            print(f"Ordinador🤖: {opciones[ordinador]}")

            if jugador == ordinador:
                print("\nHeu empatat😑!")
            elif (jugador == "1" and ordinador == "3" or
                  jugador == "2" and ordinador == "1" or
                  jugador == "3" and ordinador == "2"):
                print("\nHas guanyat🥳!!")
                puntuaciojugador += 1
                historicjugador += 1
            else:
                print("\nHas perdut😔...")
                puntuaciopc += 1

            tornar = input("\nVols seguir jugant? ").lower()

            if tornar == "si":
                continue
            else:
                with open(doc, "a") as file:
                    file.write(f"{nom} : {historicjugador}\n")
                break

    elif jugador == 2:
        print(f"Humanoide🧠 => {puntuaciojugador}")
        print(f"Ordinador🤖 => {puntuaciopc}")
        input("\nFes clic a Enter↩️  per tornar al menú ⬅️  ")

    elif jugador == 3:
        print("\n Historic de puntuacions: ")
        print("Jugador : Punts")
        print("=" * 20)

        if os.path.exists(doc):
            with open(doc, "r") as file:
                for linia in file:
                    print(linia.strip())

        input("\nFes clic a Enter↩️  per tornar al menú ⬅️  ")

    elif jugador == 4:
        print("Sortint del joc...")
        break

    else:
        print("Opció no vàlida!")