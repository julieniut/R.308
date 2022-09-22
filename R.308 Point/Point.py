import math

class Point:
    def __init__(self,x:float=0 , y:float=0):
        self.__x=x
        self.__y=y

    def __str__(self):
        return f"x={self.__x} y={self.__y}"

    def distance_cordonnees(self,a:float, b:float)->float:
        return math.sqrt((self.__x-a)*(self.__x-a)+(self.__y-b)*(self.__y-b))

    def distance_point(self,other,):
        return math.sqrt((self.__x-other.__x)*(self.__x-other.__x)+(self.__y-other.__y)*(self.__y-other.__y))

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y