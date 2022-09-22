import sys
import Personnage as perso

def main():
    profil_par_defaut = perso.Personnage()
    profil  = perso.Personnage("test",10)
    test=perso.Personnage.Soin
    print(profil_par_defaut)
    print(profil)











if __name__=="__main__":
    sys.exit(main())