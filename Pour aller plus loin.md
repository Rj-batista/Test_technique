# Pour aller plus loin 

## DataPipeline 
### Question 
Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ?
### Réponse 
L'utilisation de double boucle for dans les fonctions dict_pubmed, dict_trial, dict_final et count_drug dans le script Ad-Hoc.py augmente considérablement le temps de calcul surtout si le volume des données est non négligéable. Il y a aussi la redondance des fonctions qui opère de la même manière mais sur des zones du fichier JSON différentes (d'une partie sur "Pubmed" et de l'autre sur "Clinical_trials du fichier) ce qui augmente encore plus le temps de calcul et l'espace mémoire à gérer. 
Il est aussi question du nombre de variable notamment avec le stockage des DataFrame dans les deux programmes qui obligerait à stocker un volume de donnée pour pouvoir opérer. 

### Question 
Pourriez-vous décrire les modifications qu’il faudrait apporter, s’il y en a, pour prendre en considération de telles volumétries ?
### Réponse
Essayer de remplacer les doubles boucles for par des solutions moins couteuse en temps 
Privilégier si possible l'utilisation de générateur pour eviter de stocker autant de variable en mémoire 
Optimiser la redondance du code en condensant certaines fonctions entre-elles
