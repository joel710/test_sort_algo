def tri_insertion(liste):
    """
    Tri par insertion de la liste donnée.
    
    Arguments :
    liste -- La liste à trier
    
    Retourne :
    La liste triée
    """
    for i in range(1, len(liste)):
        cle = liste[i]
        j = i - 1
        while j >= 0 and liste[j] > cle:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = cle
    return liste

# Exemple d'utilisation :
ma_liste = [29, 10, 14, 37, 13]
print("Liste non triée:", ma_liste)
print("Liste triée:", tri_insertion(ma_liste))
