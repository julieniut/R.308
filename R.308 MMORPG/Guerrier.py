from Personnage import Personnage

class Guerrier(Personnage):
    def __init__(self, pseudo: str, niveau: int = 1):
        super().__init__(pseudo,niveau)
        self.action = niveau * 4+6
        self.pv= niveau * 8+6

    def __str__(self):
        return f"Guerrier {super().__str__()}"

    def soin(self):
        self.__pv = self.niveau*5+3

    def degats(self):
        return self.niveau*2