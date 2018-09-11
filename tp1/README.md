
# Table des matières

1.  [4TMS702U, TP1 séance 1: environnement de travail et initiation à Python](#orgf5fc7fd)
    1.  [Partie 1: environnement de travail, premiers pas avec git.](#org7e21e60)
    2.  [Partie 2: programmes de calcul en Python, utilisation de Numpy et Matplotlib](#orgfde3294)



<a id="orgf5fc7fd"></a>

# 4TMS702U, TP1 séance 1: environnement de travail et initiation à Python

**Le compte-rendu ([./CR.md](./CR.md)) utilise le [formalisme Markdown](https://guides.github.com/features/mastering-markdown) de Github.**

    - Renvoyez moi le fichier CR.md par email (yves.coudiere@u-bordeaux.fr) aujourd'hui, mardi 11 septembre 2018.
    - Indiquer [TP1.1] avec vos noms et prénom dans le sujet du mail
    - Ne pas oublier de joindre aussi les fichiers (images par exemple) vers lesquelles le fichier .md pointe éventuellement.


<a id="org7e21e60"></a>

## Partie 1: environnement de travail, premiers pas avec git.

Pour travailler, notre environnement de travail sera constitué 

-   d'un terminal et
-   d'un éditeur de texte qui vous soit familier.

Il s'agit du terminal par défaut de l'environnement du Cremi, et de
[emacs](https://www.gnu.org/software/emacs) dans mon cas. Vous pouvez éventullement utiliser un environnement
de travail intégré (IDE) dédié qui supporte git et python.

[![img](./img/ecran01.png "Voici à quoi ressemble mon écran lors de l'écriture des notes de cours.")](img/ecran01.png) 

*Note:* concernant `emacs`, il est conseillé de le configurer dans le fichier
`$HOME/.emacs`. Vous trouverez un exemple de configuration ici: [./.emacs](./.emacs).

1.  Prenez le temps de choisir votre environnement de travail en
    explorant les différentes possibilités. Donner votre choix dans le
    compte-rendu, [./CR.md](./CR.md).
2.  Cloner le dépôt (commande `git clone`), ceci créera un repertoire
    dans votre répertoire courant. Quel est le nom de ce répertoire ?
3.  Familiarisez vous avec le contenu du répertoire, qui devrait ressembler à :
    
        cours/
        ├── README.md
        └── tp1
            ├── CR.md
            ├── README.md
            ├── img
            │  ├── ecran01.png
            └── src
        	├── data_types.py
        	├── hello_world.py
        	├── ...
    
    Quel est la nature (langage ?) et le rôle (texte, programme, autre) de chacun
    des fichiers présents ?


<a id="orgfde3294"></a>

## Partie 2: programmes de calcul en Python, utilisation de Numpy et Matplotlib

1.  À partir du programme existant, calculer le tableau des erreurs
    commises par la méthode d'Euler explicite pour l'équation y'(t) = 1-y
    avec y(0) = 5 pour t dans [0,1], en prenant des pas de temps h = 0.2
    0.1 0.05 0.025 0.0125 0.00625. 
    
    Donner le tableau des valeurs et tracer le graphe de l'erreur en
    fonction de h en échelle logarithmique. Ce graphe est appelé graphe
    de convergence.
2.  Reproduire cette étude pour l'équation y'(t) = 1-y^2, dont on sait
    calculer une solution exacte. On prendra t dans [0,1] et y(0) = 0
    puis y(0)=2.
3.  Reprendre l'analyse avec la méthode suivante à la place de la méthode
    d'Euler: y\_{n+1} = y\_n + h\*f(t\_n+0.5\*h,y\_n+0.5\*f(y\_n)). Tracer les
    graphes de convergence des 2 méthodes sur la même figure (en échelle
    logarithmique). Quel commentaire peut-on faire ?
4.  Reprendre l'analyse avec la méthode y\_{n+1} = y\_{n-1} +
    2\*h\*f(t\_n,y\_n), pour laquelle on calculera y\_1 par la seconde
    méthode.
5.  On souhaite utiliser la méthode y\_{n+1} = y\_n + 0.5\*h\*( f(t\_n,y\_n) +
    f(t\_{n+1},y\_{n+1}). Il fait donc résoudre une équation non
    linéaire. Pour cela, on peut
    -   utiliser la méthode de Newton telle qu'elle existe dans le module
        `scipy.optimize`;
    -   calculer y\_{n+1} comme la limite de la suite itérative y\_{n+1,p+1}
        = y\_n + 0.5\*h\*( f(t\_n,y\_n) + f(t\_{n+1},y\_{n+1,p}) avec par exemple
        y\_{n+1,0} calculé par la méthode d'Euler explicite ou bien
        y\_{n+1,0}=y\_n.
6.  Un problème plus raide&#x2026;

