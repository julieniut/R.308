import sys
import Personnage as perso
import Guerrier as gue
import Mage as mag
import Joueur as joueur

def main():
    profil_par_defaut = perso.Personnage()
    p1 = perso.Personnage("toto",10)
    #p1.Combat(profil_par_defaut)
    guerrier = gue.Guerrier("guerrier",2)
    mage=mag.Mage("mage",2)
    #mage.Combat(guerrier)
    j = joueur.Joueur("toto")
    j.ajout(p1)
    #j.print_list()
    #print(([i.pseudo for i in j.get_list]))
    print(j)
    #print(guerrier)
    #print(mage)

    #print(f"nom {p1.get_pseudo()}")
    #print(profil_par_defaut)
    #print(p1)











if __name__=="__main__":
    sys.exit(main())