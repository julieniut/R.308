class Personnage:
    def __init__(self,pseudo:str="non assigné" , niveau:int=1):
        self.__pseudo=pseudo
        self.__niveau=niveau


    def __str__(self):
        return f"pseudo: {self.__pseudo} niveau: {self.__niveau}"

    #def Attaque(self,):


    def Soin(self):
        nb_pv=self.__niveau
        return f"nombre de points de vie {nb_pv}"
