def mostrar_menu():
    print("""MENÚ
    1. Grabar
    2. Buscar
    3. Retirarse
    4. Salir""")

def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion in(1,2,3,4):
                return opcion
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

#vamos a crear las funciones necesarias para grabar

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if len(str(rut)) >= 7 and len(str(rut)) <= 8:
                return rut
            else:
                print("ERROR! RUT INCORRECTO!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

def validar_nombre_mas():
    while True:
        nombre = input("Ingrese nombre mascota: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! NOMBRE DE LA MASCOTA DEBE TENER AL MENOS 3 LETRAS!")

def validar_dias():
    while True:
        try:
            cantidad_dias = int(input("Ingrese cantidad de días de alojamiento: "))
            if cantidad_dias >= 1:
                return cantidad_dias
            else:
                print("ERROR! LA CANTIDAD DE DÍAS DEBE SER AL MENOS 1 DÍA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

import numpy as np
hotel = np.zeros((2,5), int)
lista_ruts          = []
lista_nombres       = []
lista_ides          = []
lista_nom_mascotas  = []
lista_dias          = []
lista_filas         = []
lista_columnas      = []

def ver_hotel():
    for x in range(2):
        print(f"FILA {x+1}:", end="  ")
        for y in range(5):
            print(hotel[x][y], end=" ")
        print()
    print("COLUMNAS 1 2 3 4 5")

def validar_fila():
    while True:
        try:
            fila = int(input("Ingrese número fila(1-2): "))
            if fila >= 1 and fila <= 2:
                return fila
            else:
                print("ERROR! FILA DEBE SER 1 o 2!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO!")

def validar_columna():
    while True:
        try:
            columna = int(input("Ingrese número columna(1-5): "))
            if columna >= 1 and columna <= 5:
                return columna
            else:
                print("ERROR! COLUMNA DEBE ESTAR ENTRE 1 Y 5!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO!")

def grabar(p_contador):
    #aqui dice: SI NO HAY HABITACIONES DISPONIBLES!
    if 0 not in hotel:
        print("NO EXISTEN HABITACIONES DISPONIBLES!")
        return
    print("GRABAR DATOS")
    rut = validar_rut()
    nombre = validar_nombre()
    id_mascota = p_contador
    nombre_mas = validar_nombre_mas()
    cant_dias = validar_dias()
    #mostrar como esta el hotel:
    while True:
        ver_hotel()
        fila = validar_fila()
        columna = validar_columna()
        #debo encargarme de validar si puedo o no usar la habitacion elegida! (fila/columna) (n° habitacion)
        if hotel[fila-1][columna-1] == 0:
            hotel[fila-1][columna-1] = 1
            lista_ruts.append(rut)
            lista_nombres.append(nombre)
            lista_ides.append(id_mascota)
            lista_nom_mascotas.append(nombre_mas)
            lista_dias.append(cant_dias)
            lista_filas.append(fila-1)
            lista_columnas.append(columna-1)
            print("MASCOTA REGISTRADA!")
            return p_contador + 1
        else:
            print("UBICACIÓN NO DISPONIBLE! TA OCUPAO!")

def buscar():
    print("BUSCAR")
    rut = validar_rut()
    #buscamos si el rut esta en la lista!
    if rut in lista_ruts:
        #que necesito saber del rut encontrado, LA POSICION DE LA LISTA DONDE ESTA!
        posicion = lista_ruts.index(rut)
        print("SU MASCOTA SE LLAMA:",lista_nom_mascotas[posicion])
        print("FILA DE SU MASCOTA:",lista_filas[posicion]+1)
        print("COLUMNA DE SU MASCOTA:",lista_columnas[posicion]+1)
    else:
        print("RUT NO EXISTE!")

def retirarse():
    print("RETIRARSE")
    rut = validar_rut()
    if rut in lista_ruts:
        posicion = lista_ruts.index(rut)
        total = 15000 * lista_dias[posicion]
        print("SU TOTAL A PAGAR ES:", total)
        #debo eliminar a la mascota y dueño de las listas, Y DEJAR LA HABITACION DEL HOTEL DISPONIBLE:
        fila = lista_filas[posicion]
        columna = lista_columnas[posicion]
        #ahora voy a borrar y disponibilizar!
        lista_ruts.pop(posicion)
        lista_nombres.pop(posicion)
        lista_ides.pop(posicion)
        lista_nom_mascotas.pop(posicion)
        lista_dias.pop(posicion)
        lista_filas.pop(posicion)
        lista_columnas.pop(posicion)
        hotel[fila][columna] = 0
        print("GRACIAS, VUELVA PRONTO!")
    else:
        print("RUT NO EXISTE!")

def salir():
    print("GRACIAS POR PREFERIRNOS, ADIOS!")