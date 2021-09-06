# Pour aller plus loin 

## DataPipeline 
### Question 
Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ?
### Réponse 
L'utilisation de double boucle for dans les fonctions dict_pubmed, dict_trial, dict_final ainsi que de count_drug du script Ad-Hoc.py augmentent considérablement le temps de calcul. Ce temps est d’autant plus grande si la taille des données est non négligéable. 
Il faudrait essayer de remplacer les doubles boucles for par des solutions moins couteuses en temps.

Nous avons également la redondance des fonctions qui opère de la même manière mais sur des zones du fichier JSON différentes (d'une partie sur "Pubmed" et de l'autre sur "Clinical_trials du fichier) ce qui augmente encore plus le temps de calcul et l'espace mémoire à gérer. 

Il est aussi question du nombre de variables notamment avec le stockage des DataFrames dans les deux programmes qui oblige à stocker un volume de données pour pouvoir opérer

### Question 
Pourriez-vous décrire les modifications qu’il faudrait apporter, s’il y en a, pour prendre en considération de telles volumétries ?
### Réponse
Essayer de remplacer les doubles boucles for par des solutions moins couteuse en temps 
Nous devrions privilégier si possible l'utilisation de générateur afin d’éviter le stockage de variables.
Optimiser la redondance du code en condensant certaines fonctions entre-elles
