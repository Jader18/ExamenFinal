import os
import sys

#(Agregar agrega la ruta del directorio de donde descargo/guardo el proyecto para no configurar el PYTHONPATH)
#Direccion de mafiu para ejecutar > 
sys.path.append(r"C:/Users/MathiusZ/Desktop/ProyectoLP/ExamenFinal/DataBaseConnection")
#Direccion de Jader para ejecutar > 
#sys.path.append(r"C:\Users\Jader Mendoza\Desktop\ExamenFinalLenguajeProgramacion\DataBaseConnection")
#Direccion del Profe para ejecutar >  
#sys.path.append(r"C:\ \ \ \ \")
from dao import daoConnection
from models import clases as c
from datetime import datetime


#conexion a la base de datos
os.system('cls')
conex = daoConnection.Connection("localhost", "root", "", "pharmacydatabase")
conex.connect()


#funcion para validar que el status sea valido (solamente puede ser 1 o 2)
def validar_status(status):
    if status == 1 or status == 2:
        return True
    else:
        return False
    

#Funciones para Laboratorio
#agregar
def addLab():
    name = input("Nombre del Laboratorio: ")
    address = input("Direccion del Laboratorio: ")
    phone = input("Telefono del Laboratorio: ")
    email = input("Email del Laboratorio: ")

    laboratorio = c.Lab(name, address, phone, email, 1, None)
    daoLab = daoConnection.DaoLab(conex)
    daoLab.insert(laboratorio)
    
#editar
def editLab():
    showLab()
    id = int(input("ID del laboratorio a editar: "))
    os.system('cls')
    newName = input("Nuevo nombre del Laboratorio: ")
    newAddress = input("Nueva direccion del Laboratorio: ")
    newPhone = input("Nuevo telefono del Laboratorio: ")
    newEmail = input("Nuevo email del Laboratorio: ")
    status = int(input("Ingrese el nuevo estado: 1) Activo || 2) Inactivo: "))

    if validar_status(status):
        print("Status valido")
        daoLab = daoConnection.DaoLab(conex)
        laboratorio = c.Lab(newName, newAddress, newPhone, newEmail, status, id)
        daoLab.update(laboratorio)
    else:
        print("Status inválido. Debe ser 1 o 2.")

#mostrar
def showLab():
    daoLab = daoConnection.DaoLab(conex)
    labs = daoLab.get_all()
    print("Laboratorios de la base de datos: ")
    for lab in labs:
        print(lab)

#eliminar
def deleteLab():
    showLab()
    id = int(input("ID del Laboratorio a eliminar: "))
    daoLab = daoConnection.DaoLab(conex)
    daoLab.delete(id)

#buscar
def searchLab():
    getByName = input("Nombre del laboratorio a buscar: ")
    daoLab = daoConnection.DaoLab(conex)
    labs = daoLab.get_by_name(getByName)
    print(labs)


#menu para laboratorio
def MenuLab():
    os.system('cls')
    print("*Menu de Laboratorios*")
    print("1. Ingresar Laboratorio")
    print("2. Editar Laboratorio")
    print("3. Mostrar Laboratorios")
    print("4. Eliminar Laboratorio")
    print("5. Buscar Laboratorio")
    print("6. Salir")

def mainLab():
    opcion = 0

    while(opcion != 6): 
        MenuLab()
        opcion = int(input("Ingresa una opcion: "))

        if (opcion == 1):
            os.system('cls')
            addLab()
            os.system("pause")

        elif(opcion == 2):
            os.system('cls')
            editLab()
            os.system("pause")

        elif(opcion == 3):
            os.system('cls')
            showLab()
            os.system("pause")
        
        elif(opcion == 4):
            os.system('cls')
            deleteLab()
            os.system("pause")

        elif(opcion == 5):
            os.system('cls')
            searchLab()
            os.system("pause")

#Funciones para Proveedores 

#agregar
def addSupplier():
    name = input("Nombre del Proveedor: ")
    address = input("Direccion del Proveedor: ")
    phone = input("Telefono del Proveedor: ")
    email = input("Email del Proveedor: ")

    supplier = c.Supplier(name, address, phone, email, 1, None)
    daoSupplier = daoConnection.DaoSupplier(conex)
    daoSupplier.insert(supplier)
    
#editar
def editSupplier():
    showSupplier()
    id = int(input("ID del proveedor a editar: "))
    os.system('cls')
    newName = input("Nuevo nombre del Proveedor: ")
    newAddress = input("Nueva direccion del Proveedor: ")
    newPhone = input("Nuevo telefono del Proveedor: ")
    newEmail = input("Nuevo email del Proveedor: ")
    status = int(input("Ingrese el nuevo estado: 1) Activo || 2) Inactivo: "))
    
    if validar_status(status):
        print("Status valido")
        daoSupplier = daoConnection.DaoSupplier(conex)
        supplier = c.Supplier(newName, newAddress, newPhone, newEmail, status, id)
        daoSupplier.update(supplier)
    else:
        print("Status inválido. Debe ser 1 o 2.")

#mostrar
def showSupplier():
    daoSupplier = daoConnection.DaoSupplier(conex)
    suppliers = daoSupplier.get_all()
    print("Proveedores de la base de datos: ")
    for supplier in suppliers:
        print(supplier)

#eliminar
def deleteSupplier():
    showSupplier()
    id = int(input("ID del Proveedor a eliminar: "))
    daoSupplier = daoConnection.DaoSupplier(conex)
    daoSupplier.delete(id)

#buscar
def searchSupplier():
    getByName = input("nombre del Proveedor a buscar: ")
    daoSupplier = daoConnection.DaoSupplier(conex)
    suppliers = daoSupplier.get_by_name(getByName)
    print(suppliers)



#Funciones para items

#agregar
def addItem():
    name = input("Nombre del Item: ")
    os.system('cls')
    showLab()
    labs_id = int(input("ID del Laboratorio: "))
    os.system('cls')
    showSupplier()
    suppliers_id = int(input("ID del Proveedor: "))
    price = float(input("Precio del Item: "))
    category = input("Categoria del Item: ")
    expiration_date = input("Fecha de expiracion: (dd/mm/yyyy): ")
    description = input("Descripcion del Item: ")



    item = c.Item(name, labs_id, suppliers_id, price, category, expiration_date, description, 1, None)
    daoItem = daoConnection.DaoItem(conex)
    daoItem.insert(item)    

#editar
def editItem():
    showItem()
    id = int(input("ID del Item a editar: "))
    os.system('cls')
    newName = input("Nombre del Item: ")
    os.system('cls')
    showLab()
    newLabs_id = int(input("ID del Laboratorio: "))
    os.system('cls')
    showSupplier()
    newSuppliers_id = int(input("ID del Proveedor: "))
    newPrice = float(input("Precio del Item: "))
    newCategory = input("Categoria del Item: ")
    newExpiration_date = input("Fecha de expiracion: (dd/mm/yyyy): ")
    newDescription = input("Descripcion del Item: ")
    status = int(input("Ingrese el nuevo estado: 1) Activo || 2) Inactivo: "))
    
    if validar_status(status):
        print("Status valido")
        daoItem = daoConnection.DaoItem(conex)
        item = c.Item(newName, newLabs_id, newSuppliers_id, newPrice, newCategory, newExpiration_date, newDescription, status, id)
        daoItem.update(item)
    else:
        print("Status inválido. Debe ser 1 o 2.")

    
#mostar
def showItem():
    daoItem = daoConnection.DaoItem(conex)
    items = daoItem.get_all()
    print("Items de la base de datos: ")
    for item in items:
        print(item)

#eliminar
def deleteItem():
    showItem()
    id = int(input("ID del Item a eliminar: "))
    daoItem = daoConnection.DaoItem(conex)
    daoItem.delete(id)

#buscar
def searchItem():
    getByName = input("Nombre del Item a buscar: ")
    daoItem = daoConnection.DaoItem(conex)
    items = daoItem.get_by_name(getByName)
    print(items)


#menu para Items
def menuItems():
    os.system('cls')
    print("*Menu de Items*")
    print("1. Ingresar Item")
    print("2. Editar Item")
    print("3. Mostrar Items")
    print("4. Eliminar Item")
    print("5. Buscar Item")
    print("6. Salir")

def mainItems():
    opcion = 0

    while(opcion != 6): 
        menuItems()
        opcion = int(input("Ingresa una opcion: "))

        if (opcion == 1):
            os.system('cls')
            addItem()
            os.system("pause")

        elif(opcion == 2):
            os.system('cls')
            editItem()
            os.system("pause")

        elif(opcion == 3):
            os.system('cls')
            showItem()
            os.system("pause")
        
        elif(opcion == 4):
            os.system('cls')
            deleteItem()
            os.system("pause")

        elif(opcion == 5):
            os.system('cls')
            searchItem()
            os.system("pause")

#menu para Proveedores
def menuSupplier():
    os.system('cls')
    print("*Menu de Proveedores*")
    print("1. Ingresar Proveedor")
    print("2. Editar Proveedor")
    print("3. Mostrar Proveedores")
    print("4. Eliminar Proveedor")
    print("5. Buscar Proveedor")
    print("6. Salir")

def mainSupplier():
    opcion = 0

    while(opcion != 6): 
        menuSupplier()
        opcion = int(input("Ingresa una opcion: "))

        if (opcion == 1):
            os.system('cls')
            addSupplier()
            os.system("pause")

        elif(opcion == 2):
            os.system('cls')
            editSupplier()
            os.system("pause")

        elif(opcion == 3):
            os.system('cls')
            showSupplier()
            os.system("pause")
        
        elif(opcion == 4):
            os.system('cls')
            deleteSupplier()
            os.system("pause")

        elif(opcion == 5):
            os.system('cls')
            searchSupplier()
            os.system("pause")


#Menu principal
def mainMenu():
    os.system('cls')
    print("*Menu principal*")
    print("----------------------------")
    print("1. Registros de Laboratorios")
    print("2. Registros de Proveedores")
    print("3. Registros de Items")
    print("4. Salir")
    print("----------------------------")


def main():
    opcion= 0
    while(opcion != 4):
        mainMenu()
        opcion = int(input("Ingresa una opcion:"))
        if (opcion == 1):
            mainLab()
            os.system("pause")
        elif (opcion == 2):
            mainSupplier()
            os.system("pause")    
        elif (opcion == 3):
            mainItems()
            os.system("pause")   


main()

