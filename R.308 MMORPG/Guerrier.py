import Peronnage as Personnage

class Guerrier(Personnage):
    def __init__(self, pseudo: str, lvl: int = 1):
        Personnage(pseudo,lvl)
        super.action = lvl * 4+6
        super.pv= lvl * 4+6
    def __str__(self):
        return f"Guerrier {super().__str__()}"
    def soin(self):
        self.__pv = self.__lvl*5+3