stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1]
}

productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['Lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

def stock_marca(marca):
    marca = marca.lower()
    total = sum(
        stock[modelo][1]
        for modelo, datos in productos.items()
        if datos[0].lower() == marca and modelo in stock
    )
    print(f"El stock es: {total}") if total > 0 else print("El stock es: 0")

def busqueda_precio(p_min, p_max):
    resultados = sorted(
        (modelo, productos[modelo][0])
        for modelo, (precio, _) in stock.items()
        if p_min <= precio <= p_max and modelo in productos
    )
    return resultados

def actualizar_precio():
    while True:
        modelo = input("Ingrese modelo a actualizar: ").strip()
        if modelo not in stock:
            print("El modelo no existe!!")
        else:
            try:
                nuevo_precio = int(input("Ingrese precio nuevo: "))
                stock[modelo][0] = nuevo_precio
                print("Precio actualizado!!")
            except ValueError:
                print("Precio inválido.")
        
        seguir = input("Desea actualizar otro precio (s/n)?: ").strip().lower()
        if seguir != 'si':
            break

def mostrar_menu():
    print("\n*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese opción: ").strip()
        
        if opcion == '1':
            marca = input("Ingrese la marca: ")
            stock_marca(marca)

        elif opcion == '2':
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
            except ValueError:
                print("Debe ingresar valores enteros!!")
                continue

            resultados = busqueda_precio(p_min, p_max)

            if resultados:
                for modelo, marca in resultados:
                    print(f"{modelo} ({marca})")
            else:
                print("No hay notebooks en ese rango de precios.")

        elif opcion == '3':
            actualizar_precio()

        elif opcion == '4':
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida. Debe seleccionar una opción válida.")

main()