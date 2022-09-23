import sys
import Personnage as perso
#import Guerrier


def main():
    profil_par_defaut = perso.Personnage("toto",28)
    p1 = perso.Personnage("test",10)
    p1.Attaque(profil_par_defaut)


    #print(profil_par_defaut)
    #print(p1)











if __name__=="__main__":
    sys.exit(main())