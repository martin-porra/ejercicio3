from claseCamion import Camion
from claseCosecha import Cosecha

class Menu:
    def ejecuta(lista_camiones, cosecha):
        print('Menu\n1- Ver cantidad total de kilos descargados por un camión (Consigna 3-1).\n2- Ver informe por día (Consigna 3-2)\n3- Salir.')
        op = int(input('Seleccione opcion:'))
        while op != 3:
            if op == 1:
                aux = int(input('Ingrese numero de identificación de camión (del 1 al 20):'))
                if aux < 1 or aux > 20:
                    print('Error. Número ingresado no válido, debe ser del 1 al 20.')
                else:
                    print('Cantidad total de kilos descargados:',cosecha.GetTotalDescargadoCam(aux-1))
            elif op == 2:
                aux = int(input('Ingrese número de día (del 1 al 45):'))
                if aux < 1 or aux > 45:
                    print('Error. Número ingresado no válido, debe ser del 1 al 45.')
                else:
                    cosecha.GetInformeDia(aux,lista_camiones)
            elif op == 3:
                print('Saliendo de menú.')
            else:
                print('Error. Opción no válida.')
            print('Menu\n1- Ver cantidad total de kilos descargados por un camión (Consigna 3-1).\n2- Ver informe por día (Consigna 3-2)\n3- Salir.')
            op = int(input('Seleccione opcion:'))