# Python Data Science Training

Ce dépôt contient les exercices pour la formation Python en Science des Données. Les exercices couvrent les concepts fondamentaux de la programmation Python avec un accent sur les applications en science des données.

## Contenu

La formation est divisée en plusieurs exercices :

0. Hello World et Types de Données de Base
1. Formatage de Dates
2. Types d'Objets
3. Gestion des Valeurs Nulles
4. Nombres Pairs et Impairs
5. Comptage de Caractères
6. Fonction Filter Personnalisée et Filtrage de Chaînes
7. Encodeur en Code Morse
8. Barre de Progression Personnalisée (fonction similaire à tqdm)
9. Création d'un Package Python

## Prérequis

- Python 3.10
- Bibliothèques supplémentaires spécifiées dans les exercices individuels


## Exécution des Exercices

Chaque exercice est contenu dans son propre répertoire (ex00, ex01, etc.). Naviguez vers le répertoire de l'exercice et exécutez le script Python .

# Exercices
Training Piscine Python for data science – 00 Starting
 

### <ins>Ex00 : </ins>
 
Cet exercice a pour but de connaître les différents types de données non-primitives en Python et de savoir lesquelles sont mutables ou immuables. 

* Liste (ft_list) : Les listes sont mutables, ce qui permet de modifier directement un élément en l'indexant. 
* Tuple (ft_tuple) : Les tuples sont immuables, vous devez donc créer un nouveau tuple avec les valeurs souhaitées. 
* Set (ft_set) : Les sets sont mutables, mais comme il s'agit de collections non ordonnées, vous devez remplacer l'ensemble par un nouvel ensemble contenant les valeurs souhaitées. 
* Dictionnaire (ft_dict) : Les dictionnaires sont mutables, ce qui permet de modifier directement la valeur associée à une clé. 

 
### Ex01 : 
 
L'objectif principal de cet exercice est de s'entraîner à travailler avec des dates et des heures en Python, en se concentrant plus particulièrement sur le formatage et l'affichage de ces données de différentes manières. En réalisant cet exercice, vous acquerrez de l'expérience dans les domaines suivants : 

1. Récupérer la date et l'heure actuelles : Utilisation des modules datetime et time de Python pour obtenir la date et l'heure actuelles. 
2. Formatage des horodatages : Convertir l'heure actuelle dans un format lisible par l'homme et l'afficher dans différents formats, y compris la notation scientifique. 
3. Utilisation de techniques de formatage de chaînes de caractères : Affichage des informations relatives à la date et à l'heure dans un format spécifique, comme indiqué dans l'exemple de sortie. 

 
### Ex02 : 
 
L'objectif de cet exercice est d'écrire une fonction all_thing_is_obj qui imprime les types des objets donnés et renvoie l'entier 42. La fonction doit gérer différents types d'objets et imprimer des messages spécifiques en fonction de leurs types. Les types à traiter sont les listes, les tuples, les ensembles, les dictionnaires et les chaînes de caractères. 

### Ex03 : 

L'objectif principal de cet exercice est d'écrire une fonction nommée NULL_not_found qui prend un objet de n'importe quel type en argument et imprime le type de l'objet s'il correspond à l'un des types "NULL" (None, NaN, 0, chaîne vide ou False). Si l'objet ne correspond à aucun de ces types "NULL", la fonction doit afficher "Type not Found" et renvoyer 1. Si la fonction s'exécute sans erreur, elle doit renvoyer 0. 

 

### Ex04 : 

L'exercice est conçu pour tester et améliorer votre compréhension des éléments suivants : 

1. La gestion des arguments de la ligne de commande en Python à l'aide du module sys. 
2. Vérification du type et validation des données d'entrée. 
3. Opérations arithmétiques de base comme l'opérateur module. 
4. Gestion des erreurs et levée des exceptions en Python. 
5. Rédiger des messages d'erreur clairs et concis pour le retour d'information de l'utilisateur. 

En réalisant cet exercice, vous démontrerez votre capacité à écrire un script qui interagit avec l'utilisateur par le biais d'arguments de ligne de commande, qui effectue une validation de base des données et qui fournit des informations basées sur les données d'entrée. 

 

### Ex05 : 

En réalisant cet exercice, vous acquerrez de l'expérience dans les domaines suivants : 

1. Gérer les arguments de la ligne de commande. 
2. Valider les entrées. 
3. Compter et classer les caractères d'une chaîne. 
4. Structurer et formater la sortie. 
 

### Ex06 : 

Cet exercice est conçu pour vous aider à mettre en pratique et à intégrer ces concepts, ce qui fera de vous un programmeur Python plus compétent et plus polyvalent. 

1. Compréhension des listes (List Comprehensions): Création de listes de manière dynamique sur la base de listes existantes. 
2. Fonctions Lambda (Lambda Functions): Écriture de fonctions anonymes en ligne pour des opérations simples. 
3. Command-Line Argument Handling : Utilisation de sys.argv pour lire et valider les entrées de la ligne de commande. 
4. Error Handling : Implémentation de contrôles et levée d'exceptions pour gérer les entrées non valides. 
5. Programmation fonctionnelle (Functional Programming): Utilisation de concepts de programmation fonctionnelle tels que les filtres et les fonctions lambda. 

 

### Ex07 : 

L'objectif principal de cet exercice est de renforcer vos compétences en manipulation de chaînes de caractères, en utilisation de dictionnaires et en gestion des arguments de ligne de commande en Python. La tâche spécifique consiste à encoder une chaîne donnée en code Morse 

 

### Ex08 : 

L'objectif principal de cet exercice est de recréer la fonctionnalité de la bibliothèque tqdm en utilisant l'opérateur yield en Python. tqdm est une bibliothèque qui permet de visualiser la progression des boucles en Python avec une barre de progression. Cette tâche vous permettra de pratiquer les générateurs, la gestion du temps et la création de barres de progression. 

1. Créer la fonction ft_tqdm : Cette fonction doit imiter le comportement de tqdm en utilisant l'opérateur yield pour générer les éléments tout en affichant une barre de progression. 
2. Utiliser un générateur : Implémenter la fonction de manière à ce qu'elle puisse être utilisée comme un générateur Python. 
3. Afficher la barre de progression : Calculer et afficher la progression de la boucle de manière similaire à tqdm. 

 

### Ex09 : 

L'objectif principal de cet exercice est de vous apprendre à créer et distribuer un package Python. Vous apprendrez à organiser votre code en modules, à créer les fichiers nécessaires pour définir et configurer le package, et à utiliser des outils comme setuptools pour construire et installer le package. L'exercice comprend également la vérification que votre package apparaît dans la liste des packages installés et qu'il affiche les informations correctes avec la commande ‘pip show’. 
