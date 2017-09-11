<div id="table-of-contents">
<h2>Table des matières</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline4">1. 4TMS702U, TP1 : environnement de travail et initiation à Python</a>
<ul>
<li><a href="#orgheadline2">1.1. Partie 1: environnement de travail, premiers pas avec git.</a></li>
<li><a href="#orgheadline3">1.2. Partie 2: programmes de calcul en Python, utilisation de Numpy et Matplotlib</a></li>
</ul>
</li>
<li><a href="#orgheadline1">2. Ressources</a></li>
<li><a href="#orgheadline5">3. Foire aux questions</a></li>
</ul>
</div>
</div>


# 4TMS702U, TP1 : environnement de travail et initiation à Python<a id="orgheadline4"></a>

Y. Coudière

**Vous rédigerez un compte-rendu de travail dans le fichier [./CR.md](./CR.md), en utilisant
le [formalisme Markdown](https://guides.github.com/features/mastering-markdown).**

## Partie 1: environnement de travail, premiers pas avec git.<a id="orgheadline2"></a>

Pour travailler, notre environnement de travail sera constitué d'un terminal et
d'un éditeur de texte qui vous soit familier, il s'agit de [emacs](https://www.gnu.org/software/emacs) dans mon
cas. Vous pouvez éventullement utiliser un environnement de travail intégré
(IDE) dédié qui supporte git et python.

[![img](./img/ecran01.png "Voici à quoi ressemble mon écran lors de l'écriture des notes de cours.")](img/ecran01.png) 

*Note:* concernant `emacs`, il est conseillé de le configurer dans le fichier
`$HOME/.emacs`. Vous trouverez un exemple de configuration ici: [./.emacs](./.emacs).

1.  Prenez le temps de choisir votre environnement de travail en explorant les
    différentes possibilités. Expliquer votre choix dans le compte-rendu ([./CR.md](./CR.md)
    accessible après la question ci-dessous).
2.  Cloner le dépôt (commande `git clone`), ceci créera un repertoire `csm1` dans
    votre répertoire courant. Expliquer dans le compte-rendu les difficultés que
    vous avez eu à cette étape.
    -   **git:** voir la section [Ressources](#orgheadline1)
    -   **linux:** commandes de base, voir [ce guide](https://doc.ubuntu-fr.org/tutoriel/console_commandes_de_base) ou [celui ci](http://tdinfo.phelma.grenoble-inp.fr/docs/guideUnix.pdf) par exemple.
3.  Familiarisez vous avec le contenu du répertoire, qui devrait ressembler à :
    
        cours/
        ├── README.md
        └── tp1-decouverte
            ├── CR.md
            ├── README.md
            ├── img
            │  ├── ecran01.png
            └── src
                ├── data_types.py
                ├── hello_world.py
                ├── phase_systlin.py
    
    Quel est la nature (langage ?) et le rôle (texte, programme, autre) de chacun
    des fichiers présents ?
4.  Après avoir écrit votre compte-rendu pour cette première partie, indexez
    (commande `git add`) puis validez vos changements au fichier [./CR.md](./CR.md) (command
    `git commit`). Enfin, vous pouvez poussez votre travail sur le serveur
    distant (commande `git push`). Notez dans le compte-rendu les énoncés précis
    des commandes que vous avez utilisées.

## Partie 2: programmes de calcul en Python, utilisation de Numpy et Matplotlib<a id="orgheadline3"></a>

1.  Pour vérifier votre environnement de travail, trouvez et exécutez les
    programmes [./src/hello\_world.py](./src/hello_world.py) (affichage) et [./src/data\_types.py](./src/data_types.py) (types
    python très simples). On peut,
    
    -   soit exécuter directement les fichiers dans le terminal:
        
            $ ./src/hello_world.py
            (suppressed output)
            $ ./src/data_types.py
            (suppressed output)
    -   ou alors dans l'interpréteur `ipython`:
        
            $ ipython
            Python 3.4.5 (default, Dec  4 2016, 23:12:44) 
            Type "copyright", "credits" or "license" for more information.
            
            IPython 5.4.1 -- An enhanced Interactive Python.
            ?         -> Introduction and overview of IPython's features.
            %quickref -> Quick reference.
            help      -> Python's own help system.
            object?   -> Details about 'object', use 'object??' for extra details.
            
            In [1]: run ./src/hello_world.py
            (supressed output)
            In [2]: run ./src/data_types.py
            (supressed output)
    
    Donnez le contenu des sorties qui ont été supprimées dans ces deux
    exemples. *N'oubliez pas de validez à chaque étape*, `git add` *et* `git
       commit`.
2.  On considère l'équation différentielle \(y'' + by = a^2 = 0\). Une solution \(y\)
    est aussi une solution du système linéaire d'ordre un \(Z' = - AZ\) ou \(Z = (y,
       y')\) et \(A\) est une matrice. Le programme [./src/phase\_systlin.py](./src/phase_systlin.py) permet de
    tracer les lignes de courant du plan de phase \(Z=(y, y')\). Faites varier les
    valeurs prises par les coefficients \(a\) et \(b\) et illustrez les différents
    comportement de l'équation: oscillateur parfaitement harmonique, oscillateur
    amorti, et oscillateur amplifié. Explicitez les comportement dans le
    compte-rendu. On pourra inclure des images (voir le guide du formalisme
    Markdown). *Encore une fois, on indexe et on valide les réponses du fichier
    de compte-rendu*.
3.  La solution exacte de cette équation s'exprime de manière analytique (je vous
    laisse la déterminer). En ajoutant du code au fichier [./src/phase\_systlin.py](./src/phase_systlin.py),
    calculez la solution exacte ayant la valeur initiale \(Z(0) = (y(0),y'(0)) =
       (\alpha,\beta)\), sur un intervalle de temps \([0,T]\) échantilloné en \(N>0\)
    sous-intervalles égaux. Pour quelques valeurs de \((\alpha,\beta)\), 
    -   tracez les trajectoires solutions exactes dans le plan de phase (sur les
        champs de vecteurs déjà obtenus);
    -   tracer sur un graphe séparé les solutions \(y(t)\) en fonction de \(t\).

# Ressources<a id="orgheadline1"></a>

-   Tutoriel (fr) pour une utilisation simple de Git:
    <http://yannesposito.com/Scratch/fr/blog/2009-11-12-Git-for-n00b/>
-   Lire le chapitre 2 (les bases) du libre Git, <https://git-scm.com/book/fr/v2>
-   Tutorial (en, 20 min &#x2013; pas pendant le TP) sur youtube, "Learn Github in 20
    minutes": <https://www.youtube.com/watch?v=0fKg7e37bQE>
-   On trouve de nombreux tutoriels sur youtube.
-   Tutoriel (en) sur le processus de travail Git:
    <https://www.atlassian.com/git/tutorials/comparing-workflows>
-   Formalisme Markdown: <https://guides.github.com/features/mastering-markdown>

# Foire aux questions<a id="orgheadline5"></a>

-   Pourquoi utiliser Github pour les TP et projets ? Chaque projet logiciel doit
    utiliser un système de contrôle du code. Github est un système moderne et
    répandu pour le développement logiciel. Il est basé sur git, un système de
    gestion de version concurrentes, de type distribué. La connaissance d'un tel
    système est un atout important sur le marché du travail.

-   Faut-il connaître les commandes git pour utiliser Github ? Il sera utile
    d'être familier avec quelques commandes. Il existe aussi des interfaces
    graphiques (environnements de développement) pour git ou Github, si vous le
    souhaitez.

-   Comment est-ce que j'installe git ?  Github suppose que git et installé sur
    votre ordinateur. Voir les tutoriels ci-dessus, qui expliquent comment
    l'installer.

-   Est-ce que je peux utiliser un autre système que je connais, par exemple svn,
    butbucket ou mercurial ? Non, puisque nous utilisons Git Classromm dans ce
    cours.

<https://classroom.github.com/a/FDn1tAoQ>
