from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente

# Entrada principal del programa
def ejecutar_menu():

    servicio_restaurante = Restaurante()
    #   Bucle principal del menú
    while True:
        print("\n" + "=" * 40)
        print("        SISTEMA DE RESTAURANTE")
        print("=" * 40)
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("-" * 40)
        print("4. Registrar cliente")
        print("5. Listar clientes")
        print("6. Buscar cliente")
        print("-" * 40)
        print("7. Salir")

        opcion = input("Seleccione una opción (1-7): ").strip()
        # Capturar errores de validación y otros errores
        try:
            if opcion == "1":
                print("\n--- Registrar Nuevo Producto ---")
                nombre = input("Nombre del producto: ")
                categoria = input("Categoría: ")
                precio = float(input("Precio: "))

                # Creación dinámica de objeto
                nuevo_producto = Producto(nombre, categoria, precio)
                servicio_restaurante.registrar_producto(nuevo_producto)
                print("¡Producto registrado con éxito!")

            elif opcion == "2":
                print("\n--- Lista de Productos ---")
                productos = servicio_restaurante.listar_productos()
                if not productos:
                    print("No hay productos registrados.")
                for prod in productos:
                    print(prod.mostrar_informacion())

            elif opcion == "3":
                print("\n--- Buscar Producto ---")
                nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
                prod_encontrado = servicio_restaurante.buscar_producto(nombre_buscar)
                if prod_encontrado:
                    print(f"\nResultado:\n{prod_encontrado.mostrar_informacion()}")
                else:
                    print("Producto no encontrado.")

            elif opcion == "4":
                print("\n--- Registrar Nuevo Cliente ---")
                id_cliente = input("ID/Cédula del cliente: ").strip()
                if not id_cliente:
                    print("El ID no puede estar vacío.")
                    continue
                nombre = input("Nombre completo: ").strip()
                correo = input("Correo electrónico: ").strip()

                # Creación dinámica de objeto Cliente   
                nuevo_cliente = Cliente(nombre, correo, id_cliente)
                servicio_restaurante.registrar_cliente(nuevo_cliente)
                print("¡Cliente registrado con éxito!")

            elif opcion == "5":
                print("\n--- Lista de Clientes ---")
                clientes = servicio_restaurante.listar_clientes()
                if not clientes:
                    print("No hay clientes registrados.")
                for cli in clientes:
                    print(cli.mostrar_informacion())

            elif opcion == "6":
                print("\n--- Buscar Cliente ---")
                id_buscar = input("Ingrese el ID del cliente a buscar: ")
                cli_encontrado = servicio_restaurante.buscar_cliente(id_buscar)
                if cli_encontrado:
                    print(f"\nResultado:\n{cli_encontrado.mostrar_informacion()}")
                else:
                    print("Cliente no encontrado.")

            elif opcion == "7":
                print("\nGracias por usar el sistema. ¡Hasta pronto!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

        except ValueError as e:
            print(f"\n[Error de Validación]: {e}. Operación cancelada.")
        except Exception as e:
            print(f"\n[Error inesperado]: {e}")


if __name__ == "__main__":
    ejecutar_menu()
