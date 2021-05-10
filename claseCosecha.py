import numpy as np
from claseCamion import Camion

class Cosecha:
    __arrecosecha = np.empty((20,45),dtype=float) #Crea arreglo numpy bidimensional, 20 camiones (filas), 45 dias (columnas), tipo float
    def __init__(self):
        for i in range (20):
            for j in range (45):
                self.__arrecosecha[i][j] = 0
    def acumulakilos(self,idcam,dia,kilosbruto,tara):
        if type(idcam) is int and type(dia) is int and type(kilosbruto) is float and type(tara) is float:
            self.__arrecosecha[idcam][dia] += (kilosbruto - tara)
    def GetTotalDescargadoCam(self,idcam):
        acum = 0
        if type(idcam) is int:
            for j in range (45):
                acum += self.__arrecosecha[idcam][j]
        return acum
    def GetInformeDia(self,dia,lista_camiones):
        print('PATENTE CONDUCTOR CANTIDAD DE KILOS')
        if type(dia) is int:
            for i in range (20):
                pat = lista_camiones[i].GetPatente()
                conduc = lista_camiones[i].GetConductor()
                print('{} {} {}'. format(str(pat),str(conduc),self.__arrecosecha[i][dia-1]))