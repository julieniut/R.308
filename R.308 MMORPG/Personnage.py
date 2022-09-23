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
            opposant.pv-= self.__niveau
            print(f"{self.__pseudo} attaque {opposant.__pseudo} pv {opposant.pv}")
            if opposant.pv >0:
                self.pv -= opposant.__niveau
                print(f"{opposant.__pseudo} attaque {self.__pseudo} pv {self.pv}")
        elif opposant.action>self.action:
            self.pv-= opposant.__niveau
            print(f"{opposant.__pseudo} attaque {self.__pseudo} pv {self.pv}")
            if self.pv>0:
                opposant.pv -= self.__niveau
                print(f"{self.__pseudo} attaque {opposant.__pseudo} pv {opposant.pv}")
        else:
            opposant.pv-=self.__niveau
            self.pv-= opposant.__niveau
        print(f"{self.__pseudo} à  {self.pv} pv et {opposant.__pseudo} à {opposant.pv} pv")

    def Combat(self, opposant):
        while (self.pv > 0 and opposant.pv > 0):
            self.Attaque(opposant)

    def Soin(self):
        self.pv=self.__niveau
