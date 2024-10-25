from productos import Camisa, Pantalon, Zapato
from carri import Carrito

def mostrar_menu():
    print("Seleccione un producto para agregar al carrito:")
    print("1. Camisa Azul - 25.99 Gs")
    print("2. Pantalón Negro - 39.99 Gs")
    print("3. Zapato Deportivo - 59.99 Gs")
    print("4. Salir")

def guardar_compras(resumen):
    with open('data.txt', 'a') as file:
        file.write(resumen + '\n')

def main():
    carrito = Carrito()
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número del producto que desea agregar (o 4 para salir): ")

        if opcion == '1':
            camisa = Camisa("Camisa Azul", 25.99, "M", "Algodón", "Clásico")
            carrito.agregar_producto(camisa)
            print("Camisa Azul agregada al carrito.")
        elif opcion == '2':
            pantalon = Pantalon("Pantalón Negro", 39.99, "L", "Denim", "Slim")
            carrito.agregar_producto(pantalon)
            print("Pantalón Negro agregado al carrito.")
        elif opcion == '3':
            zapato = Zapato("Zapato Deportivo", 59.99, "42", "Cuero", "Deportivo")
            carrito.agregar_producto(zapato)
            print("Zapato Deportivo agregado al carrito.")
        elif opcion == '4':
            print("Saliendo del menú.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

    resumen = carrito.mostrar_resumen()
    print(resumen)
    guardar_compras(resumen)

if __name__ == "__main__":
    main()

