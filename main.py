import csv
import numpy  as np  # Arreglos NumPy
from claseCamion import Camion
from claseCosecha import Cosecha


def test():
 print('Función test. Cargue los datos de una instancia camión.')
 iden = int(input('Ingrese numero de identificacion (del 1 al 20):'))
 cond = str(input('Ingrese nombre del conductor:'))
 pat = str(input('Ingrese patente:'))
 mar = str(input('Ingrese marca:'))
 tar = float(input('Ingrese tara:'))
 prueba = Camion(iden, cond, pat, mar, tar)
 +print('Instancia camión de prueba creada.')


if __name__ == '__main__':
 lista_camiones = []
 archivo = open('archivoCamiones.txt')
 reader = csv.reader(archivo, delimiter=',')
 for fila in reader:
    unCamion = Camion(int(fila[0]), fila[1], fila[2], fila[3], float(fila[4]))
    lista_camiones.append(unCamion)
 archivo.close()
 print('Lista de camiones cargada.')
 arrecos = Cosecha()
 archivo = open('archivoCosecha.txt')
 reader = csv.reader(archivo, delimiter=',')
 for fila in reader:
    tar = lista_camiones[fila[0]].GetTara()
    arrecos.acumulakilos(int(fila[0]) - 1, int(fila[1]) - 1, float(fila[2]), tar)
 archivo.close()
 print('Cosecha cargada.')
