def mostrar_menu():
    """Mostra el menu"""
    print(" Funcions 2")
    print("====================")
    print("1. Comptar majúscules i minúscules")
    print("2. Any de traspàs")
    print("3. Dies del mes")
    print("4. Número perfecte")
    print("0. Sortir")
def introduir_int_segur(missatge, minim=None, maxim=None):
    """Demana un enter vàlid i el retorna"""
    ok = False

    while ok is not True:
        valor = input(missatge)

        if valor.isdigit():
            valor = int(valor)

            if minim is not None and valor < minim:
                print(f"El número ha de ser més gran o igual que {minim}.")

            elif maxim is not None and valor > maxim:
                print(f"El número ha de ser més petit o igual que {maxim}.")

            else:
                ok = True

        else:
            print("Has de ser un número enter: ")

    return valor
def comptar_majuscules_minuscules(cadena):
    """Compta les majúscules i minúscules d'una cadena"""
    m = 0
    maj = 0

    for i in range(len(cadena)):
        if cadena[i].islower():
            m = m + 1
        elif cadena[i].isupper():
            maj = maj + 1

    return (maj, m)
def es_any_traspas(a):
    """Comprova si un any és de traspàs."""

    if a % 400 == 0:
        return True

    elif a % 100 == 0:
        return False

    elif a % 4 == 0:
        return True

    else:
        return False
def comptar_dies_mes(mes, a):
    """Retorna el nombre de dies d'un mes en un any determinat"""
    dies = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if mes == 2 and es_any_traspas(a):
        dies[1] = 29

    return dies[mes - 1]
def es_num_perfecte(numero):
    """Comprova si un número és perfecte"""
    suma = 0

    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma == numero


def main():
    opcio = 10
    while opcio != 0:
        mostrar_menu()
        opcio = introduir_int_segur("Tria una opció: ", 0, 5)
        
        if opcio == 1:
            cadena = input("Introdueix una cadena de text: ")
            comptar_majuscules_minuscules(cadena)
            maj, min = comptar_majuscules_minuscules(cadena)
            print(f"Majúscules: {maj}")
            print(f"Minúscules: {min}")
        elif opcio == 2:
            a = introduir_int_segur("Introdueix un any: ", 1)
            if es_any_traspas(a):
                print(f"L'any {a} és de traspàs.")
            else:
                print(f"L'any {a} no és de traspàs.")
        elif opcio == 3:
            mes = introduir_int_segur("Mes (1-12): ", 1, 12)
            a = introduir_int_segur("Any: ", 1)

            resultat = comptar_dies_mes(mes, a)
            print(f"El mes {mes} de l'any {a} té {resultat} dies.")
        elif opcio == 4:
            numero = introduir_int_segur("Introdueix un numero enter positiu: ", 1)
            if es_num_perfecte(numero):
                print(f"El número {numero} és perfecte.")
            else:
                print(f"El número {numero} no és perfecte.")
    
    
    
if __name__ == "__main__":
    main()
