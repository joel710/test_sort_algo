def quickSort(liste):
    if len(liste) < 2:
        return liste
    else:
        pivot = liste[0]  # Choix du premier élément comme pivot
        gauche = [elem for elem in liste[1:] if elem <= pivot]
        droite = [elem for elem in liste[1:] if elem > pivot]
        return quickSort(gauche) + [pivot] + quickSort(droite)

# Exemple d'utilisation :
ma_liste = [29, 10, 14, 37, 13]
print("Liste non triée:", ma_liste)
print("Liste triée:", quickSort(ma_liste))
