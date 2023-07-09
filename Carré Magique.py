# Créé par chari, le 13/01/2023 en Python 3.7

#Bibliothèque
import random

#Fonctions

def creation(n):
    """
    rôle : Fonction principale qui permet de la création du tableau
    entrée : n (demandé à l'utilisateur)
    précondition : n doit être demandé à l'utilisateur (n >=2)
    sortie : le résultat est la liste tab sous format tableau
    """
    liste_carré =[n for n in range(n**2)] #liste des éléments de 1 à n²
    tab=[]
    for i in range(n): #nbr de lignes
        ligne=[]
        for j in range(n): #nbr de colonnes
            ligne.append(liste_carré.pop(random.randint(0,len(liste_carré)-1)))
        tab.append(ligne)
    return tab


def affiche(tab):
    """
    rôle : Fonction qui permet l'affiche le tableau ligne par ligne
    entrée : paramètre tab
    précondition : /
    sortie : le résultat est la liste ligne par ligne
    """
    for ligne in range(0,len(tab)):
        for colonne in range(0,len(tab)):
            print(tab[ligne][colonne], end="\t")
        print("")

def pairs(tab):
    """
    rôle : Fonction qui prend en paramètre le tableau puis retourne la liste des nombres pairs uniquement
    entrée : paramètre tab
    précondition : /
    sortie : le résultat est la liste des nombres pairs
    """
    tab_pairs = []
    for i in range(0,len(tab)): #i=numéro ligne
        for j in range(0,len(tab)): #j=numéro colonne
            if tab[i][j]%2==0:
                tab_pairs.append(tab[i][j])
    return tab_pairs

def somme_colonnes(tab):
    """
    rôle : Fonction qui prend en paramètre le tableau retourne la liste des sommes des colonnes
    entrée : paramètre tab
    précondition : /
    sortie : le résultat est la liste des sommes des colonnes
    """
    somme = 0
    tab_somme_colonne = []
    for ligne in range(0,len(tab)):
        for colonne in range(0,len(tab)):
            somme += tab[colonne][ligne]
        tab_somme_colonne.append(somme)
        somme = 0
    return tab_somme_colonne


def somme_lignes(tab):
    """
    rôle : Fonction qui prend en paramètre le tableau retourne la liste des sommes des lignes
    entrée : paramètre tab
    précondition : /
    sortie : le résultat est la liste des sommes des lignes
    """
    somme = 0
    tab_somme = []
    for ligne in range(0,len(tab)):
        for colonne in range(0,len(tab)):
            somme += tab[ligne][colonne]
        tab_somme.append(somme)
        somme = 0
    return tab_somme

def somme_diagonale(tab):
    """
    rôle : Fonction qui prend en paramètre le tableau retourne la liste des sommes des diagonales
    entrée : paramètre tab
    précondition : /
    sortie : le résultat est la liste des sommes des deux diagonales
    """
    somme = 0
    tab_somme = []
    for i in range(0,len(tab)):
        somme += tab[i][i]
    tab_somme.append(somme)
    somme = 0
    for i in range(0, len(tab)):
        somme += tab[i][len(tab)-1-i]
    tab_somme.append(somme)
    return tab_somme

def est_magique(tab):
    """
    rôle : Fonction qui prend en paramètre le tableau puis retourne un booléen
    entrée : paramètre tab
    précondition : /
    sortie : retourne le booléen True si la somme des lignes + des colonnes + des diagonales est la même, sinon retourne False
    """
    diago = somme_diagonale(tab)
    if diago[0] == diago[1]:
        diago.append(diago[0])
    if somme_lignes(tab) == somme_colonnes(tab) == diago:
        return True
    else:
        return False

#Main
n = int(input("Choississez un nombre supérieur ou égal à 2 : "))
while n<2 :
    n = int(input("Erreur, merci de choisir un nombre  supérieur ou égal à 2 : "))
tab = creation(n)
##tab = [[2,7,6],[9,5,1],[4,3,8]] #Pour tester la fonction est magique et avoir un true
affiche(tab)
print("la liste des nombres pairs est :", pairs(tab))
print("la somme des colonnes est :", somme_colonnes(tab))
print("la somme des lignes est :", somme_lignes(tab))
print("la somme des diagonales est :", somme_diagonale(tab))
print(est_magique(tab))
