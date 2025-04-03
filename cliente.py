import requests #Se instala con pip install requests

base_url = "http://127.0.0.1:5000/libreria"

def consultarPrecio():
    titulo = input("Ingrese el título del libro: ")
    
    if titulo.lower() == "salir":
        return False
    
    #Enviamos la solicitud GET al servidor Flask
    params = {"titulo": titulo}
    response = requests.get(f"{base_url}/precio", params=params)

    if response.status_code == 200:
        data = response.json()
        if data['precio'] != -1:
            print(f"El precio de '{data['titulo']}' es: ${data['precio']}\n")
        else:
            print("Libro no encontrado.\n")
    else:
        print(f"Error al conectarse al servicio. Código: {response.status_code}\n")
    return True

def agregarLibro():
    titulo = input("Ingrese el título del nuevo libro: ")
    
    if titulo.lower() == "salir":
        return False
    
    try:
        precio = float(input("Ingrese el precio del libro: $"))
    except ValueError:
        print("El precio debe ser un número válido.\n")
        return True
    
    # Preparamos los datos para la solicitud POST
    datos = {
        "titulo": titulo,
        "precio": precio
    }
    
    # Enviamos la solicitud POST al servidor Flask
    response = requests.post(f"{base_url}/libro", json=datos)
    
    if response.status_code == 201:
        data = response.json()
        print(f"Libro '{data['libro']['titulo']}' agregado correctamente con precio: ${data['libro']['precio']}\n")
    else:
        print(f"Error al agregar el libro. Código: {response.status_code}")
        print(f"Respuesta: {response.text}\n")
    return True

def mostrarMenu():
    print("\n===== BIBLIOTECA =====")
    print("1. Consultar precio de un libro")
    print("2. Agregar un nuevo libro")
    print("3. Salir")
    return input("Seleccione una opción (1-3): ")

def main():
    continuar = True
    
    while continuar:
        opcion = mostrarMenu()
        
        if opcion == "1":
            continuar = consultarPrecio()
        elif opcion == "2":
            continuar = agregarLibro()
        elif opcion == "3":
            print("¡Hasta luego!")
            continuar = False
        else:
            print("Opción no válida. Por favor, intente de nuevo.\n")

if __name__ == "__main__":
    main()