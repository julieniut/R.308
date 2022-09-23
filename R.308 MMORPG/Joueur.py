import Personnage as perso

class Joueur:
    def __int__(self, nom: str, list_perso: list = []):
        self.__nom = nom
        self.__list_perso = list_perso

    def __str__(self):
        return f"{self.__nom} -> Personnage {self.__list_perso}"


    def ajout(self, Personnage):
        return self.__list_perso.append(Personnage)


    def get_perso(self):
        return

