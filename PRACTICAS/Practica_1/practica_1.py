import os
import csv

class AplicacionProductos:
    def __init__(self):
        pass

    def run(self):
        while True:
            obj_login_productos = LoginProductos()
            credenciales = obj_login_productos.inicio_sesion()
            obj_administrador = Administrador()

            if obj_administrador.validar_credenciales(credenciales):
                os.system("cls")
                print("BIENVENIDO!")
                obj_navegacion = Navegacion()
                obj_navegacion.desplegar_opciones()
                break
            else:
                os.system("cls")
                print("CREDENCIALES NO VALIDAS\n")

class Administrador:
    def __init__(self):
        self._usuario = "admin"
        self._password = "123"
    
    def validar_credenciales(self, credenciales):
        return credenciales == [self._usuario, self._password]

class LoginProductos:
    def __init__ (self):
        pass

    def inicio_sesion(self):
        print("CRUD PRODUCTOS")
        print("----------------------------------------------------")
        usuario = input("Usuario: ")
        password = input("Contraseña: ")
        credenciales = [usuario, password]
        return credenciales

class Navegacion:
    def __init__(self):
        self._gestion_productos = GestionProductos()

    def desplegar_opciones(self):
        while True:
            print("SISTEMA DE GESTION DE PRODUCTOS")
            print("----------------------------------------------------")
            print("1.- Registrar producto")
            print("2.- Listar todos los productos")
            print("3.- Modificar un producto")
            print("4.- Eliminar un producto")
            print("5.- Salir")
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                self._gestion_productos.registrar_producto()
            elif opcion == 2:
                self._gestion_productos.listar_productos()
            elif opcion == 3:
                self._gestion_productos.modificar_producto()
            elif opcion == 4:
                self._gestion_productos.eliminar_producto()
            elif opcion == 5:
                print("Hasta luego!")
                print("Saliendo del sistema...")
                break
            else:
                os.system("cls")
                print("Opcion no valida, intente de nuevo")

class Productos:
    def __init__(self, id, nombre, precio, cantidad):
        self._id = id
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad
    
    def get_id(self):
        return self._id
    def set_id(self, id):
        self._id = id
    
    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def get_precio(self):
        return self._precio
    def set_precio(self, precio):
        self._precio = precio
    
    def get_cantidad(self):
        return self._cantidad
    def set_cantidad(self, cantidad):
        self._cantidad = cantidad
    
    def mostrar_producto(self):
        print(f"ID: {self._id}")
        print(f"Nombre: {self._nombre}")
        print(f"Precio: {self._precio}")
        print(f"Cantidad: {self._cantidad}")

class GestionProductos:
    def __init__(self):
        self._lista_productos = self.cargar_productos_desde_csv()
    
    def cargar_productos_desde_csv(self):
        lista_productos = []
        try:
            with open("productos.csv", mode = "r", newline = "", encoding = "utf-8") as archivo:
                reader = csv.reader(archivo)
                for row in reader:
                    if row:
                        id, nombre, precio, cantidad = row
                        lista_productos.append(Productos(id, nombre, precio, cantidad))
        except FileNotFoundError:
            pass
        return lista_productos
    
    def guardar_productos_en_csv(self):
        with open("productos.csv", mode = "w", newline = "", encoding = "utf-8") as archivo:
            writer = csv.writer(archivo)
            for producto in self._lista_productos:
                writer.writerow([producto.get_id(), producto.get_nombre(), producto.get_precio(), producto.get_cantidad()])
    
    def registrar_producto(self):
        os.system("cls")
        print("REGISTRO DE PRODUCTO")
        print("----------------------------------------------------")
        id = input("ID del producto: ")
        nombre = input("Nombre del producto: ")
        precio = input("Precio del producto: ")
        cantidad = input("Cantidad disponible: ")

        producto = Productos(id, nombre, precio, cantidad)
        self._lista_productos.append(producto)
        self.guardar_productos_en_csv()

        os.system("cls")
        print("Producto registrado exitosamente")
    
    def listar_productos(self):
        if len(self._lista_productos) == 0:
            os.system("cls")
            print("No hay productos registrados para listar.")
        else:
            os.system("cls")
            print("LISTA DE PRODUCTOS")
            print("----------------------------------------------------")
            for producto in self._lista_productos:
                producto.mostrar_producto()
                print("----------------------------------------------------")
            input("Presione una tecla para continuar...")
            os.system("cls")
    
    def modificar_producto(self):
        if len(self._lista_productos) == 0:
            os.system("cls")
            print("No hay productos registrados para modificar.")
        else:
            os.system("cls")
            id = input("Ingrese el ID del producto a modificar: ")
            producto_encontrado = False

            for producto in self._lista_productos:
                if producto.get_id() == id:
                    producto_encontrado = True
                    print("Producto encontrado")
                    print("1. Modificar nombre")
                    print("2. Modificar precio")
                    print("3. Modificar cantidad")
                    opcion = int(input("Seleccione una opción: "))

                    if opcion == 1:
                        nuevo_nombre = input("Nuevo nombre: ")
                        producto.set_nombre(nuevo_nombre)
                    elif opcion == 2:
                        nuevo_precio = input("Nuevo precio: ")
                        producto.set_precio(nuevo_precio)
                    elif opcion == 3:
                        nueva_cantidad = input("Nueva cantidad: ")
                        producto.set_cantidad(nueva_cantidad)
                    else:
                        print("Opción no válida.")

                    print("Producto modificado exitosamente")
                    self.guardar_productos_en_csv()
                    os.system("cls")
                    break
            
            if not producto_encontrado:
                print("Producto no encontrado con ese ID.")
    
    def eliminar_producto(self):
        if len(self._lista_productos) == 0:
            os.system("cls")
            print("No hay productos registrados para eliminar.")
        else:
            os.system("cls")
            id = input("Ingrese el ID del producto a eliminar: ")
            producto_encontrado = False

            for producto in self._lista_productos:
                if producto.get_id() == id:
                    producto_encontrado = True
                    self._lista_productos.remove(producto)
                    print("Producto eliminado exitosamente")
                    self.guardar_productos_en_csv()
                    break

            if not producto_encontrado:
                print("Producto no encontrado con ese ID.")

app_productos = AplicacionProductos()
app_productos.run()