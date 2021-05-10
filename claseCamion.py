class Camion:
    __identi = 0 # Número de identificación (de 1 a 20)
    __conductor = '' # Nombre del conductor
    __patente = ''
    __marca = '' # Marca del camión
    __tara = 0.0 # Tara: peso del camión vacío
    def __init__(self, numid, cond, pat, marc, tar):
        if type(numid) is int:
            self.identi = numid
        if type(cond) is str:
            self.__conductor = cond
        if type(pat) is str:
            self.__patente = pat
        if type(marc) is str:
            self.__marca = marc
        if type(tar) is float:
            self.__tara = tar
    def GetTara(self):
        return self.__tara
    def GetPatente(self):
        return self.patente
    def GetConductor(self):
        return self.__conductor