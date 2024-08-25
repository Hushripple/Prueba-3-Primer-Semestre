#DESARROLLO PRUEBA 3
import funciones as fn

contador = 1
while True:
    fn.mostrar_menu()
    opcion = fn.validar_opcion()
    if opcion==1:
        contador = fn.grabar(contador)
    elif opcion==2:
        fn.buscar()
    elif opcion==3:
        fn.retirarse()
    else:
        fn.salir()
        break