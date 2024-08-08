# Python Data Science Training

Ce dépôt contient les exercices pour la formation Python en Science des Données, axée sur la manipulation d'arrays et le traitement d'images.

## Contenu

La formation est divisée en plusieurs exercices :

0. Give my BMI : Calcul de BMI et application de limites
1. 2D array : Manipulation de tableaux 2D
2. Load my image : Chargement et affichage d'images
3. Zoom on me : Zoom et affichage d'une partie d'image
4. Rotate me : Rotation et transposition d'image
5. Pimp my image : Application de filtres de couleur sur des images

## Prérequis

- Python 3.10
- Bibliothèques : numpy, PIL (ou toute autre bibliothèque de manipulation d'images)

## Exécution des Exercices

Chaque exercice est contenu dans son propre répertoire (ex00, ex01, etc.). Naviguez vers le répertoire de l'exercice et exécutez le script Python correspondant.

# Exercices

Training Piscine Python for data science – 01 Array

### <ins>Ex00 : Give my BMI</ins>

Cet exercice vise à créer deux fonctions :

- `give_bmi` : Calcule l'IMC à partir de listes de tailles et de poids.
- `apply_limit` : Applique une limite à une liste d'IMC.

### <ins>Ex01 : 2D array</ins>

L'objectif est de créer une fonction `slice_me` qui manipule un tableau 2D, affiche sa forme et retourne une version tronquée du tableau en fonction des arguments de début et de fin fournis.

### <ins>Ex02 : Load my image</ins>

Développez une fonction `ft_load` qui charge une image, affiche son format et son contenu en pixels au format RGB. La gestion des formats JPG et JPEG est requise.

### <ins>Ex03 : Zoom on me</ins>

Créez un programme qui charge l'image "animal.jpeg", affiche des informations sur celle-ci (taille, nombre de canaux, contenu des pixels) et effectue un zoom sur une partie de l'image.

### <ins>Ex04 : Rotate me</ins>

Le programme doit charger l'image "animal.jpeg", en extraire une partie carrée, la transposer et afficher le résultat. La transposition doit être implémentée manuellement, sans utiliser de fonction de bibliothèque.

### <ins>Ex05 : Pimp my image</ins>

Développez 5 fonctions pour appliquer différents filtres de couleur aux images :

- `ft_invert` : Inverse les couleurs
- `ft_red` : Filtre rouge
- `ft_green` : Filtre vert
- `ft_blue` : Filtre bleu
- `ft_grey` : Conversion en niveaux de gris
