import Point as monpoint
import sys
import Cercle as moncercle
import Rectangle as monrectangle
def main():
    p1= monpoint.Point(5,7)
    #p2= monpoint.Point(2,8)

    C1=moncercle.Cercle(4, p1)
    Surface=moncercle.Cercle.CercleSurface(4)
    Diametre=moncercle.Cercle.CercleDiametre(4)
    Périmètre=moncercle.Cercle.CerclePérimètre(4)

    R1=monrectangle.Rectangle(p1,2,3)
   # print(p1.distance_cordonnees(5,8))
   # print(p1.distance_point(p2))
    print(C1)
    print(Surface)
    print(Diametre)
    print(Périmètre)

    print(R1)


if __name__=="__main__":
    sys.exit(main())