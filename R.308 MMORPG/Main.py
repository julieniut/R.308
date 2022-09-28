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
    print(guerrier)
    print(mage)
    #guerrier.Combat(mage)
    #mage.Combat(guerrier)


    j = joueur.Joueur("Joueur 1")
    j.ajout(p1)
    j.ajout(guerrier)
    j.ajout(mage)
    j.ajout(p1)

    #j.supprimer(p1)
    #joueur.Joueur.supprimer_joueur(j)

    print(f"nom {p1.get_pseudo()}") #avoir le nom du personne p1
    print(j.print_list()) #affichier la list du joueurs jS


#découverte de pickle

import pickle
import string
L = list(string.ascii_letters)
print(L)
with open('mypicklefile', 'wb') as f1:
    pickle.dump(L, f1)
with open('mypicklefile', 'rb') as f1:
    print(pickle.load(f1))
with open('mypicklefile', 'rb') as f1:
    O=pickle.load(f1)
    if L==O:
        True
t=j.print_list()
with open('mypicklefile', 'wb') as f1:
    pickle.dump(t, f1)






if __name__=="__main__":
    sys.exit(main())