
def menu():
    print("Menú principal")
    print("1-Sumar")
    print("2-Salir")


def suma(num1,num2):
    return num1+num2



def principal():
    try:
        menu()
        opciones = int(input("Elige una de las opciones:\n"))
        while opciones!= 2:
            if opciones==1:
                try:
                    num1 = int(input("Dime un número para sumarlo:\n"))
                    num2 = int(input("Dime un otro para sumarlo:\n"))
                    sum=suma(num1,num2)
                    print("La suma es",sum)
                except: print("Tienes que introducir números para poder sumarlos")
            menu()    
            opciones = int(input("Elige una de las opciones:\n"))
        print("Has terminado el programa")
    except: print("Tienes que introducir una de las dos opciones(1 o 2)")

principal()
