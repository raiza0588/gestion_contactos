#Desarrolla un programa en Python que permita al usuario almacenar, buscar y eliminar contactos de una agenda. 
#Cada contacto debe tener un nombre, número de teléfono y dirección de correo electrónico.
#lista de diccionarios
contacts = [
    {"nombre": "rafael", "telefono": "1234567678", "email": "rafa0110@gmail.com"}
]

#definicion de funciones
def add_contact(nombre, telefono, email):
    contacts.append({"nombre": nombre, "telefono": telefono, "email": email})
    print(f"Lista de contactos: {contacts}")
    return print("contacto agregado")

def search_contact(nombre):
    for contacto in contacts:
        if contacto["nombre"] == nombre:
            return contacto
    return None

def delete_contact(nombre):
    for i, contacto in enumerate(contacts):
        if contacto["nombre"] == nombre:
            del contacts[i]
            return print("Contacto eliminado!")
    return print("Contacto no encontrado")

#menu del programa
opcion = 1
while opcion != 0:
    print()
    print("Bienvenido a tu libreta de contactos")
    print("selecciona la opción que deseas realizar")
    print("1 Agregar nuevo contacto")
    print("2 Buscar contacto")
    print("3 Eliminar contacto")
    print("0 salir")
    opcion = int(input("Ingresa una opción: "))
    print("")

    #opciones de acuerdo al valor agregado
    if opcion == 1:
        print("Ingresa los datos del nuevo contacto")
        nombre = input("Escribe el nombre del nuevo contacto: ")
        telefono = input("Escribe el teléfono del nuevo contacto: ")
        email = input("Escribe el email del contacto: ")
        add_contact(nombre, telefono, email)
    elif opcion == 2:
        nombre = input("Escribe el nombre del contacto a buscar: ")
        contacto = search_contact(nombre)
        if contacto:
            print(contacto)
        else:
            print("Contacto no encontrado")
    elif opcion == 3:
        nombre = input("Ingresa el nombre del contacto a eliminar: ")
        delete_contact(nombre)
    elif opcion == 0:
        print("Hasta luego!")
        break
    else:
        print("Opcion no reconocida intenta de nuevo porfavor!")
