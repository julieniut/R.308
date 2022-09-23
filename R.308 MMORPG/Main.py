import sys
import Personnage as perso
import Guerrier as gue
import Joueur as joueur

def main():
    profil_par_defaut = perso.Personnage("bot")
    p1 = perso.Personnage("toto",10)
    p1.Combat(profil_par_defaut)
    guerrier = gue.Guerrier("guerrier",2)
    #j=joueur.Joueur(guerrier)

    print(guerrier)


    #print(profil_par_defaut)
    #print(p1)











if __name__=="__main__":
    sys.exit(main())