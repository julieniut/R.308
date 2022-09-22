from Point import Point
from math import pi

class Cercle:
        def __init__(self,rayon:float=0 , centre :Point=None):
            self.__rayon=rayon
            if centre !=None:
                self.__centre=centre
            else:
                self.__centre =Point(0,0)


        def CercleSurface(rayon):
            return f"l'aire du cercle est {format(pi*rayon * rayon,'.2f')}"

        def CercleDiametre(rayon):
            return f"le Diamètre est {rayon*2}"

        def CerclePérimètre(rayon):
            return f"le Périmètre est { format(2*pi*rayon,'.2f')}"

        #def CercleIntersection(autreCercle,Cercle):




        def __str__(self):
            return f"le rayon du cercle est {self.__rayon}, centre:{self.__centre}"




