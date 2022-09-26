class Personnage:
    def __init__(self,pseudo:str="non assigné" , niveau:int=1,soin=int):
        self.__pseudo=pseudo
        self.__niveau=niveau
        self.pv = niveau
        self.action = niveau
        self.soin = soin

    def __str__(self):
        return f"pseudo: {self.__pseudo} niveau: {self.__niveau}  point de vie {self.pv}  et {self.action} point d'inisiative"

    def get_pseudo(self):
        return self.__pseudo

    def get_niveau(self):
        return self.__niveau

    def degats(self):
        return self.__niveau

    def Attaque(self,opposant):
        if self.action > opposant.action:
            opposant.pv-= self.degats
            print(f"{self.__pseudo} attaque {opposant.__pseudo} pv {opposant.pv}")
            if opposant.pv >0:
                self.pv -= opposant.degats
                print(f"{opposant.__pseudo} attaque {self.__pseudo} pv {self.pv}")
        elif opposant.action>self.action:
            self.pv-= opposant.degats
            print(f"{opposant.__pseudo} attaque {self.__pseudo} pv {self.pv}")
            if self.pv>0:
                opposant.pv -= self.degats
                print(f"{self.__pseudo} attaque {opposant.__pseudo} pv {opposant.pv}")
        else:
            opposant.pv-=self.degats
            self.pv-= opposant.degats
        print(f"{self.__pseudo} à {self.pv} pv et {opposant.__pseudo} à {opposant.pv} pv")

    def Combat(self, opposant):
        while (self.pv > 0 and opposant.pv > 0):
            self.Attaque(opposant)

    def Soin(self):
        self.pv=self.pv
