class Personnage:
    def __init__(self,pseudo:str="non assigné" , niveau:int=1,soin=int):
        self.__pseudo=pseudo
        self.__niveau=niveau
        self.__pv = niveau
        self.__action = niveau
        self.soin = soin


    def __str__(self):
        return f"pseudo: {self.__pseudo} niveau: {self.__niveau}  point de vie {self.__pv}  et {self.action} point d'inisiative"

    @property
    def pv(self,pv):
        self.__pv=pv

    @pv.setter
    def pv(self,pv):
        self.__pv= pv

    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self,action):
         self.__action=action

    @property
    def pseudo(self):
        return self.__pseudo

    @property
    def niveau(self):
        return self.__niveau

    def degats(self):
        return self.__niveau

    def Attaque(self,opposant):
        if self.__action > opposant.__action:
            opposant.__pv-= self.degats()
            print(f"{self.__pseudo} attaque {opposant.__pseudo} pv {opposant.__pv}")
            if opposant.__pv >0:
                self.__pv -= opposant.degats()
                print(f"{opposant.__pseudo} attaque {self.__pseudo} pv {self.__pv}")
        elif opposant.__action>self.__action:
            self.__pv-= opposant.degats()
            print(f"{opposant.__pseudo} attaque {self.__pseudo} pv {self.__pv}")
            if self.__pv>0:
                opposant.__pv -= self.degats()
                print(f"{self.__pseudo} attaque {opposant.__pseudo} pv {opposant.__pv}")
        else:
            opposant.__pv-=self.degats()
            self.__pv-= opposant.degats()
        print(f"{self.__pseudo} à {self.__pv} pv et {opposant.__pseudo} à {opposant.__pv} pv")

    def Combat(self, opposant):
        while (self.__pv > 0 and opposant.__pv > 0):
            self.Attaque(opposant)

    def Soin(self):
        self.__pv=self.__pv
