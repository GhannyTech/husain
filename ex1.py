#a
from datetime import date   

def mostrar_menu():
    """Mostra el menu"""
    print(" Funcions 1")
    print("====================")
    print("1. Multiplica")
    print("2. Anys 2000")
    print("3. Gira del revés")
    print("4. Triangle de Pascal")
    print("5. Sortir")
def multiplica(a,b):
    """Multiplica dos nombres enters i mostra el resultat"""
    print(f"{a} x {b} = {a*b}")
def anys():
    """Calcula els anys que han passat des del 2000"""
    any_actual = date.today().year
    c = input(f"Introdueix un any entre 2000 i {any_actual}: ")
    ok = False

    while ok is not True:
        if c.isdigit() and 2000 <= int(c) <= any_actual:
            ok = True
        else:
            c = input(f"Torna a provar. Introdueix un any entre 2000 i {any_actual}: ")

    c = int(c)
    operacio = c - 2000
    print(f"Des del 2000 han passat {operacio} anys")
def reversa():
    """Gira una cadena de text"""
    frase_girada = ""
    frase = input("Introdueix una frase: ")
    for i in range(len(frase) - 1, -1, -1):
        frase_girada += frase[i]
        
    print(frase_girada)
def triangle_pascal():
    """Mostra el triangle de Pascal"""
    n = input("Nombre de files (entre 2 i 10): ")
    ok = False

    while ok is not True:
        if n.isdigit() and 2 <= int(n) <= 10:
            ok = True
        else:
            n = input("Ha de ser un número entre 2 i 10: ")
    n = int(n)
    
    fila = [1]
    for i in range(n):
        print(" " * (n - i - 1), end="")

        for numero in fila:
            print(numero, end=" ")

        print()

        nova_fila = [1]

        for j in range(len(fila) - 1):
            nova_fila.append(fila[j] + fila[j + 1])

        nova_fila.append(1)
        fila = nova_fila

def main ():

    opcio = 10
    
    while opcio != 5:
        mostrar_menu()
        ok = False
        while ok is not True:
            
            opcio = input("Tria un opcio: ")
            if opcio.isdigit() and 1 <= int(opcio) <= 5:
                ok = True 
            else:
                opcio = input("Torna a provar: ")
        opcio = int(opcio)   


        if opcio == 1:
            a = input("Escriu el primer nombre(enter): ")
            ok = False
            while ok is not True:
                if a.isdigit():
                    ok = True
                else:
                    a = input("Torna a provar. Escriu el primer nombre(enter): ")
            a = int(a)
            b = input("Escriu el segon nombre(enter): ")
            ok = False
            while ok is not True:
                if b.isdigit():
                    ok = True
                else:
                    b = input("Torna a provar. Escriu el segon nombre(enter): ")
            b = int(b)
            
            multiplica(a,b)
        elif opcio == 2:
            anys()
        elif opcio == 3:
            reversa()
            
        elif opcio == 4:
            triangle_pascal()
if __name__ == "__main__":
    main()
