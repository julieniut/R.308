from Point import Point


class Rectangle:
    def __init__(self,pointBG : Point=Point(0,0), longeurs:float=1,hauteur:float=1,pointHD :Point=None):
        self.__pointBG=pointBG
        self.__longueur=longeurs
        self.__hauteur=hauteur
        if pointHD!=None:
            self.__longueur= pointHD.get_x()-pointBG.get_x()
            self.__hauteur= pointHD.get_y()-pointBG.get_y()

    def __str__(self):
        return f" pointBG {self.__pointBG}, Longeur {self.__longueur}, Hauteur {self.__hauteur} "

    def surface(self):
        return self.__hauteur * self.__longueur

    def perimetre(self):
        return 2*(self.__longueur + self.__hauteur)

    def getPointBG(self)-> Point:
        return self.__pointBG

    def getPointBD(self) -> Point:
        p: Point=Point (self.__pointBG.get_x()+self.__longueur, self.__pointBG.get_y())
        return p

    def getPointHD(self) -> Point:
        p: Point=Point (self.__pointBG.get_x()+self.__longueur, self.__pointBG.get_y()+self.__hauteur)
        return p


    def appartient(self,p:Point) ->bool:
        res = False
        if self.__pointBG.get_x()+self.__longueur > p.get_x() > self.__pointBG.get_x() and self.__pointBG.get_y()+self.__hauteur:
            res = True
        return res