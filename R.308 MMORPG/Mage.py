from Personnage import Personnage
class Mage (Personnage):
    def __init__(self, pseudo: str, niveau: int = 1):
        super().__init__(pseudo, niveau)
        self.action = niveau * 6 + 4
        self.pv = niveau * 5 + 10
        self.__mana=niveau*5

    def __str__(self):
        return f"Mage {super().__str__()}"

    def soin(self):
        self.__pv = self.__niveau*5+10
        self.__mana = self.__niveau *5


    def degats(self)-> int:
        degat = super().degats()
        if self.__mana > 4:
            degat += 3
            self.__mana -= 4
        return degat

    @property
    def mana(self):
        return self.__mana
