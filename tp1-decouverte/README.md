<div id="table-of-contents">
<h2>Table des matières</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline1">1. Instructions envoyées par email</a></li>
<li><a href="#orgheadline2">2. Travail Pratique</a></li>
<li><a href="#orgheadline3">3. Resources</a></li>
<li><a href="#orgheadline4">4. Instructions pour les projets en groupes</a></li>
<li><a href="#orgheadline5">5. Foire aux questions</a></li>
</ul>
</div>
</div>


# Instructions envoyées par email<a id="orgheadline1"></a>

Nous utiliserons la plateforme Github (<https://github.com>) pour tout le travail
de ce cours (notes, comptes-rendus, programmes, résultats, etc).

1.  Rendez-vous sur <https://github.com> et créez un compte gratuit, si vous n'en
    avez pas encore.

Github vous permet de créer un dépôt de fichiers pour chacun de vos projets
(i.e. pas seulement ceux de ce cours). Mais Github n'autorise qu'un petit nombre
de dépôts privés par utilisateur. Nous utiliserons donc *Github Classroom* qui
vous donnera accès à un dépôt privé pour chaque projet à réalisé pendant le
cours.

1.  Pour créer un tel dépôt, il vous suffit d'accepter le lien d'invitation que
    je vous ai envoyé par email (sur l'email *prenom.nom@etu.u-bordeaux.fr*).

# Travail Pratique<a id="orgheadline2"></a>

1.  Environnement de travail. Pour travailler, nous avons besoin d'un terminal et
    d'un éditeur de texte qui vous soit familier. 
    
      [![img](./img/ecran01.png "Voici à quoi ressemble mon écran lors de l'écriture des notes de cours.")](img/ecran01.png) 
    Si vous utilisez `emacs`, il est conseillé de configurer emacs dans le
    fichier `$HOME/.emacs`. Vous trouverez un exemple de configuration ici:
    [<./.emacs>](.emacs). Prenez le temps de mémoriser que
    
    -   Cloner le dépôt, ceci créera un repertoire csm1 dans votre répertoire
        courant (commandes linux de base, voir
        <https://doc.ubuntu-fr.org/tutoriel/console_commandes_de_base> ou
        <http://tdinfo.phelma.grenoble-inp.fr/docs/guideUnix.pdf> par exemple).
    -   Familiarisez vous avec le contenu du répertoire, qui devrait ressembler à :
    
        cours/
        ├── README.md
        └── tp1-decouverte
            ├── README.md
            └── img
                ├── ecran01.png
2.  Vous pouvez maintenant faire des tests avec les programmes
    [<./src/hello_world.py>](src/hello_world.py) (affichage) et [<./src/data_types.py>](src/data_types.py) (types très
    simples). Pour cela, on peut 
    -   soit exécuter directement les fichiers dans le terminal:
        
            $ ./src/hello_world.py 
            $ ./src/data_types.py
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

# Resources<a id="orgheadline3"></a>

-   Tutoriel (fr) pour une utilisation simple de Git:
    <http://yannesposito.com/Scratch/fr/blog/2009-11-12-Git-for-n00b/>
-   Lire le chapitre 2 (les bases) du libre Git, <https://git-scm.com/book/fr/v2>
-   Tutorial (en, 20 min &#x2013; pas pendant le TP) sur youtube, "Learn Github in 20
    minutes": <https://www.youtube.com/watch?v=0fKg7e37bQE>
-   On trouve de nombreux tutoriels sur youtube.
-   Tutoriel (en) sur le processus de travail Git:
    <https://www.atlassian.com/git/tutorials/comparing-workflows>

# Instructions pour les projets en groupes<a id="orgheadline4"></a>

1.  Pour un projet en groupe de deux personnes ou plus, un seul membre doit
    accepter le lien d'invitation. Celui-ci doit alors aller sur le dépôt créé,
    dans l'onglet *settings*, et ajouter les autres membres en tant que
    *Collaborators and team*. Si deux membres d'un même groupe acceptent
    l'invitation, deux dépôts sontcréé, alors qu'un seul est nécessaire pour
    chaque groupe.

2.  Vous pouvez ensuite écrire du code, valider des additions et correctifs et
    les pousser sur le dépôts, et chaque membre peut alors se mettre à jour avec
    le dépôt.

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
