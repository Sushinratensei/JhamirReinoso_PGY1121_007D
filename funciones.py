import numpy 
import os 
import msvcrt
import time
lista_ruts = []
lista_nombres = []
lista_asientos = []
lista_fila = []
lista_columnas = []
lista_totales_pl = []
lista_totales_gol = []
lista_totales_sil = []
lista_totales = []
filas = [1,2,3,4,5,6,7,8,9,10]
columnas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
p_platinum = 120000
p_gold = 80000
p_silver = 50000
asientos = numpy.zeros((10,10),int)
cant_pl = []
cant_gol = []
cant_sil = []
lista_cantidad = []

def mostrar_menú():
    os.system('cls')
    print("""Menú opciones
    1. Comprar entradas
    2. Mostrar ubicaciones
    3. Ver listado asistentes
    4. Total de ganancias
    5. Salir""")

def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in (1,2,3,4,5):
                return opc
            else:
                print("Opción inválida")
        except:
            print("Error, solo números enteros")

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut sin puntos ni dígito verificador: "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("Rut inválido")
        except:
            print("Error, solo números enteros")

def validar_nombre():
    while True:
        nombre = input("Ingrese su nombre: ")
        if len(nombre.strip(" ")) >=3 and nombre.isalpha:
            return nombre
        else:
            print("Nombre inválido")

def ver_escenario():
    for x in range(10):
        print("\tA", "\tB", "\tC", "\tD", "\tE", "\tF", "\tG", "\tH", "\tI", "\tJ")
        print("Fila", filas[x], end="\t")
        for y in range(10):
            print(asientos[x][y],end="\t")
        print()
    time.sleep(5)
        
def validar_cant_persona():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad de entradas a comprar: "))
            if cantidad >= 1 and cantidad <=3:
                return cantidad
            else:
                print("Cantidad muy grande, solo aceptamos comprar 3 entradas")
        except:
            print("Error, solo números enteros")

def validar_fila():
    while True:
        try:
            fila = int(input("Ingrese Fila: "))
            if fila in filas:
                return fila
        except:
            print("Fila no válida, solo use números enteros")

def validar_columna():
    while True:
        columna = input("Ingrese columna: ")
        if columna.upper in columnas:
            return columna
        
def total_cant():
    total_cant = cant_pl + cant_gol + cant_sil
    return total_cant

def total_gan():
    ganancias = lista_totales_pl + lista_totales_gol + lista_totales_sil
    return ganancias

def validar_entrada():
    while True:
        try:
            entrada = int(input("ingrese tipo de entrada, 1.Platinum, 2.Golden, 3.Silver: "))
            if entrada in (1,2,3):
                return entrada
            else:
                print("Entrada inccorrecta")
        except:
            print("Error, debe ser número entero")

def buscar(posicion):
    rut = validar_rut()
    for x in range(len(lista_ruts)):
        if x in lista_ruts:
            x = posicion 
        


def comprar():
    acumulador_pl = 0
    acumulador_gol = 0
    acumulador_sil= 0
    cantidad = 0
    rut = validar_rut()
    nombre = validar_nombre()
    entrada = validar_entrada()
    cantidad = validar_cant_persona()
    fila = validar_fila()
    columna = validar_columna()
    if entrada ==1:
        print("Debe pagar:$", cantidad * p_platinum)
        total_pl = cantidad * p_platinum
        lista_totales_pl.append(total_pl)
        cant_pl.append(cantidad)
        acumulador_pl += total_pl
    elif entrada ==2:
        print("Debe pagar:$",cantidad * p_gold)
        total_gol = cantidad * p_gold
        lista_totales_gol.append(total_gol)
        cant_gol.append(cantidad)
        acumulador_gol += total_gol
    else:
        print("Debe pagar:$", cantidad * p_silver)
        total_sil = cantidad * p_silver
        lista_totales_sil.append(total_sil)
        cant_sil.append(cantidad)
        acumulador_sil += total_sil
    lista_ruts.append(rut)
    lista_nombres.append(nombre)
    lista_asientos.append(fila, columna)
    acumulador = acumulador_pl + acumulador_gol + acumulador_sil
    lista_totales.append(acumulador)
    cantidad = cant_pl + cant_gol + cant_sil
    lista_cantidad.append(cantidad)
    

        
def total_ganancias():
    print(f"""
    TIPO ENTRADA         CANTIDAD                   TOTAL
    ---------------------------------------------------------------
    PLATINUM            {cant_pl}             ${lista_totales_pl}
    ---------------------------------------------------------------
    GOLDEN              {cant_gol}            ${lista_totales_gol}
    ---------------------------------------------------------------
    SILVER              {cant_sil}            ${lista_totales_sil}  
    ---------------------------------------------------------------
    TOTAL              {lista_cantidad}                ${lista_totales} """)
    time.sleep(5)