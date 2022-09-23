from Personnage import Personnage

class Joueur:
    def __init__(self, nom: str, list_perso: list = []):
        self.__nom = nom
        self.__list_perso = list_perso

    def __str__(self):
        return f"{self.__nom} -> Personnage {self.__list_perso}"


    def ajout(self, Personnage):
         self.__list_perso.append(Personnage)

    #def print_list(self):
     #   print([joueur.pseudo for joueur in self.__list_perso])

    def get_list(self):
        return self.__list_perso