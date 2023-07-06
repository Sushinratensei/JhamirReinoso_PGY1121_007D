import funciones as fn

while True:
    fn.mostrar_menú()
    opcion = fn.validar_opcion()
    if opcion == 1:
        fn.comprar()
    elif opcion ==2:
        fn.ver_escenario()
    elif opcion ==3:
        fn.buscar()
    elif opcion ==4:
        fn.total_ganancias()
    else:
        print("""Jhamir Reinoso
        (06/07/2023)""")
        break