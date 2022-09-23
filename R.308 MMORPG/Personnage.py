class Personnage:
    def __init__(self,pseudo:str="non assigné" , niveau:int=1,soin=int):
        self.__pseudo=pseudo
        self.__niveau=niveau
        self.pv = niveau
        self.action = niveau
        self.soin = soin

    def __str__(self):
        return f"pseudo: {self.__pseudo} niveau: {self.__niveau} point de vie et {self.action} point d'inisiative"

    def Attaque(self,opposant):
        if self.action > opposant.action:
            opposant.pv-= self.degats()
            if opposant.pv >0:
                self.pv -= opposant.degats()
        elif opposant.action>self.action:
            self.pv-= opposant.degats()
            if self.pv>0:
                opposant.pv -= self.degats()
        else:
            opposant.pv-=self.degats()
            self.pv-= opposant.degats()

    def Combat(self, opposant):
        while (self.pv > 0 and opposant.pv > 0):
            self.Attaque(opposant)

    def Soin(self):
        self.pv=self.__niveau
