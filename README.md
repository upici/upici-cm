
# Table des matières

1.  [Organisation pratique, évaluation](#org21d6162)
    1.  [Les objectifs principaux](#orge4d6586)
    2.  [La méthode pour y arriver](#org5db2dee)
    3.  [Évaluation](#org707063e)
    4.  [Emploi du temps](#orge04bc14)
    5.  [Codes UE et groupes](#org9c40488)
    6.  [Tentative de déroulement](#orgf22c9f5)
2.  [Outils et resources](#orgfbdff6b)
    1.  [Git](#org7857fa7)
    2.  [Latex, Markdown](#org90da346)
    3.  [Python](#org9ebe2b8)
    4.  [EDP et calcul scientifique](#org14b45e9)
3.  [Quelques mots sur le calcul scientifique (dans ce cours)](#org17cc17f)
    1.  [Introduction](#org7a12db6)
    2.  [Des problèmes spécifiques](#orga97f943)
    3.  [Matériel](#org8f32445)
    4.  [Outils informatiques](#org26e37d8)
    5.  [Mathématiques](#org1eb0749)
    6.  [Objectif principal](#orgf936121)
    7.  [Liens](#org357a5bb)
4.  [Python et les modules scientifiques](#org633bc93)
    1.  [Généralités](#org707cb8e)
    2.  [Python pour le calcul scientifique](#org12f2e4f)
    3.  [Interpéteur](#orgcb1ece7)
    4.  [Disponibilité, installation](#org4087549)



<a id="org21d6162"></a>

# Organisation pratique, évaluation


<a id="orge4d6586"></a>

## Les objectifs principaux

-   Découvrir les possibilités d'un langage de haut niveau pour le calcul
    scientifique, dans notre cas Python avec les modules Numpy, Scipy, Matplotlib,
    etc.
-   Découvrir l'approximation des EDP par la pratique.


<a id="org5db2dee"></a>

## La méthode pour y arriver

Travailler en groupe collaboratifs, en présentiel et à distance: apprentissage
par projets et séances de mise en commun.

Chaque groupe de 3 ou 4 étudiants a en charge la réalisation d'un projet. Le
projet est réalisé pendant les heures de TP et librement en dehors. Chaque
projet donne lieu à

-   un compte rendu hebdomadaire d'avancement;
-   un temps d'échange après quelques séances;
-   la réalisation d'un compte-rendu terminal;
-   un exposé devant l'ensemble des étudiants.


<a id="org707063e"></a>

## Évaluation

-   Session 1 : 0.7\*rapport + 0.3\*contrôle continu (présentation + cr hebdomadaires)
-   Session 2 : 0.7\*2e version du rapport + 0.3\*max(contrôle continu de
    session 1, note rapport session 2), ie règle du max


<a id="orge04bc14"></a>

## Emploi du temps

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-right" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-right">CM1</td>
<td class="org-left">mardi 11/09/2018</td>
<td class="org-left">9:30 12:30</td>
<td class="org-left">A28/CREMI/105</td>
<td class="org-left">Introduction à git, latex, python</td>
</tr>


<tr>
<td class="org-right">1</td>
<td class="org-left">mardi 18/09/2018</td>
<td class="org-left">9:30 12:30</td>
<td class="org-left">A28/CREMI/105</td>
<td class="org-left">TP1 individuel</td>
</tr>


<tr>
<td class="org-right">2</td>
<td class="org-left">mardi 02/10/2018</td>
<td class="org-left">9:30 12:30</td>
<td class="org-left">A28/CREMI/105</td>
<td class="org-left">Début travail en groupes</td>
</tr>


<tr>
<td class="org-right">3</td>
<td class="org-left">mardi 09/10/2018</td>
<td class="org-left">9:30 12:30</td>
<td class="org-left">A28/CREMI/105</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-right">4</td>
<td class="org-left">mardi 16/10/2018</td>
<td class="org-left">9:30 12:30</td>
<td class="org-left">A28/CREMI/105</td>
<td class="org-left">Tour de table mise en commun</td>
</tr>


<tr>
<td class="org-right">5</td>
<td class="org-left">mardi 06/11/2018</td>
<td class="org-left">9:30 12:30</td>
<td class="org-left">A28/CREMI/105</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-right">6</td>
<td class="org-left">mardi 13/11/2018</td>
<td class="org-left">9:30 12:30</td>
<td class="org-left">A28/CREMI/105</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-right">7 (opt)</td>
<td class="org-left">mardi</td>
<td class="org-left">9:30 12:30</td>
<td class="org-left">A28/CREMI/105</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-right">CM2</td>
<td class="org-left">mardi</td>
<td class="org-left">9:30 12:30</td>
<td class="org-left">A28/CREMI/105</td>
<td class="org-left">Présentation finale des projets</td>
</tr>
</tbody>
</table>


<a id="org9c40488"></a>

## Codes UE et groupes

-   **Code UE:** 4TMS702U
-   **Codes groupes:** 4TAQ702S pour "Analyse, EDP, proba" et 4TQM701S
    pour tronc commun "EDP - Modélisation - Approximation".
-   **Email du groupe:** ue-4tms702u@diffetu.u-bordeaux.fr


<a id="orgf22c9f5"></a>

## Tentative de déroulement

1.  CM1: intro, cadre du cours, exemples, planning, dates importantes,
    travail à fournir, échanges. Bref cours sur git, python, markdown à
    partir d'un exemple de code et de compte-rendu en latex, qui
    deviendra le TP1 à terminer à la prochaine séance.

2.  TP1, individuel: gestion individuel d'un projet git. Rédaction d'un
    premier compte-rendu en Markdown. Prise en main de python: faire
    réaliser un petit code à chacun. Utilisation de ipython + editeur de
    texte. Pour traiter un système de 2 EDO à la place d'une EDO unique,
    puis tracer les trajectoires dans le plan de phase. Discussion et
    explication des sujets, choix et organisation en groupes.

3.  TP2-3: Premier travail de programmation sur une situation simplifiée
    du projet. Reflexion sur les difficultés supplémentaires pour le cas
    'final', quelles sont les questions auxquelles répondre ? Où trouver
    les réponses ? Comment organiser le travail à venir ? Rédaction d'un
    rapport préliminaire en latex si possible.

4.  TP4: tour de table pour que chaque groupe synthétise son rapport,
    ses qestions, son cheminement. Commencer le travail final de
    programmation.

5.  TP5-6: travail de programmation sur le projet, et mise au point, via
    les resources disponibles, et par échange avec l'enseignant.

6.  TP7: finalisation du projet, rédaction en commun du squelette du
    rapport, mise en place des éléments les plus importants, notamment
    les résultats disponibles. Répartition du travail de rédaction et de
    mise en forme. Rédaction du plan de l'exposé, nombre de diapos,
    contenu et rôle de chaque diapo.

7.  CM2: exposé par groupe, remise des rapports finaux.


<a id="orgfbdff6b"></a>

# Outils et resources

Plus d'informations dans le premier TP, et plus d'informations disponible au fur
et à mesure de l'avancement du cours.


<a id="org7857fa7"></a>

## Git

-   L'outil Git, par l'intermédiaire de la plateforme, <http://github.com>
-   <http://yannesposito.com/Scratch/fr/blog/2009-11-12-Git-for-n00b/>
-   <https://www.miximum.fr/blog/enfin-comprendre-git/>
-   <https://openclassrooms.com/courses/gerez-vos-codes-source-avec-git>


<a id="org90da346"></a>

## Latex, Markdown

-   Le langage Markdown, pour l'écriture de compte-rendus hebdomadaires, <https://daringfireball.net/projects/markdown>
-   Le langage Latex, <https://www.latex-project.org>


<a id="org9ebe2b8"></a>

## Python

-   Le langage Python (et les modules cités plus haut), <https://www.python.org>
-   Les modules dédiés au calcul scientifique,
    <https://www.scipy.org/about.html>, licences libres variées.
-   Il existe de nombreuses autres resources pour python.


<a id="org14b45e9"></a>

## EDP et calcul scientifique

Vous avez accès à la bibliothèque de math et info (bâtiment A33).


### Livres à la BMI

-   Sainsaulieu, Lionel. Calcul scientifique. Cours et exercices corrigés
    pour le 2ème cycle et les écoles d'ingénieurs. Deuxième édition. -
    Dunod, 2000.
-   Filbet, Francis. Analyse numérique : algorithme et étude
    mathématique. 2e édition. - Dunod, 2013. - ( Sciences Sup ).
-   Quarteroni, Alfio & Sacco, Riccardo & Saleri, Fausto. Méthodes
    numériques - algorithmes, analyse et applications. - Springer
    Verlag, 2007.
-   Quarteroni, Alfio. Numerical models for differential problems. -
    Springer Verlag, 2009. - ( Modeling, Simulation & Applications ; 2).
-   Quarteroni, Alfio & Valli, Alberto. Numerical approximation of partial
    differential equations. - Springer Verlag, 1994. - ( Springer Series
    in Computational Mathematics ; 23).
-   Tveito, Aslak & Winther, Ragnar. Introduction to partial differential
    equations. A computational approach. - Springer Verlag, 1998. - (
    Texts in applied mathematics ; 29).
-   Dautray, Robert & Lions, Jacques-Louis. Analyse mathématique et calcul
    numérique pour les sciences et les techniques ; Volumes 1 à 9 -
    Masson, 1987-1988. - (Collection Enseignement).


### Autres livres

-   Elements of Scientific Computing. Authors: Tveito, A., Langtangen,
    H.P., Nielsen, B.F., Cai, X. Springer 2010.
-   Fundamentals of Scientific Computing. Authors: Gustafsson,
    Bertil. Springer 2011.


### Lien web


<a id="org17cc17f"></a>

# Quelques mots sur le calcul scientifique (dans ce cours)


<a id="org7a12db6"></a>

## Introduction

L'objectif est de découvrir quelques environnements de travail qui
facilitent le développement de solutions basée sur le calcul
scientifique (et l'utilisation de plateformes de calcul haute
performance). Le cours vise **la simulation numérique de modèles** issus
de la physique, de la biologie, etc, et **basés sur des équations aux
dérivées partielles**.

En sciences, le calcul scientifique est un outil à part entière de
résolution de problèmes et de conception de solutions techniques. Il
existe désormais plusieurs outils matures qui facilitent et accélèrent
le développement de ces solutions techniques. La maîtrise de ces outils
et du calcul scientifique est un atout important de la recherche
d'emploi.

Quelques questions importantes à propos du calcul scientifique:

-   Quelles plateformes matérielles, quels outils informatiques, quelles
    méthodes mathématiques ?
-   Comment assurer la reproductibilité des résultats ? Quelles sont les
    bonnes pratiques de programmation pour cela (gestion de versions &#x2013;
    git, svn&#x2026; &#x2013;, tests, documentation&#x2026;) ?


<a id="orga97f943"></a>

## Des problèmes spécifiques

Des problèmes d'ingénierie ou de recherche qui demande la résolution de
problèmes numériques de très grandes tailles ou qui sont très nombreux.

Exemple de la prévision de la météo, de gestion de files d'attente complexes
(réseaux chemin de fer, réseaux avions&#x2026;), du traitement d'image (imagerie
médicale, animation&#x2026;)

L'ordinateur fait des + et \*, et répartit le travail, communique des nombres. Le
coeur des algorithmes repose sur la gestion (construction, manipulation,
opérations&#x2026;) des grands tableaux de nombres. Et donc d'un point de vue
mathématique sur l'algèbre linéaire pour des grandes matrices. Grand = plusieurs
millions, voir des milliards. Exemple: un cube 100\*100\*100 = 1 million.

À partir de ces opérations matricielles, nous allons construire des algorithmes
qui permettent de calculer des solutions approchées d'équations aux dérivées
partielles.


<a id="org8f32445"></a>

## Matériel

-   **Ordinateurs portable:** faibles performances mais très répandus, en
    général multicoeur à mémoire partagée.
-   **Stations de travail fixes:** meilleures performances, multicoeur ou
    multiprocesseur à mémoire partagé.
-   **Serveurs de calcul:** performances importantes à très importantes,
    nombreuses architectures possibles, mais modèles hiérarchique et
    complexes difficiles à programmer. Cf cours de calcul parallèle du
    semestre de printemps.


<a id="org26e37d8"></a>

## Outils informatiques

-   **bibliothèques:** qui permettent d'accéder aux fonctionnalités du
    matériels, comme MPI et autres techniques de
    communication ou gestion de la mémoire et de
    l'exécution (openMP), mais aussi les bibliothèques de
    calcul matriciel (BLAS, LAPACK, UMFPACK, HIPS,
    MUMPS&#x2026;).
-   **langages de programmation:** Fortran, C, C++, proches de la machine,
    utilisent directement les bibliothèques.
-   **langages de haut niveaux:** sans compilation, avec interface simplifié
    et intuitive avec les bibliothèques, temps de développement
    raccourci, maintien plus simple, interface intuitive avec les
    bibliothèques&#x2026;


<a id="org1eb0749"></a>

## Mathématiques

-   Les problèmes sont souvent du domaine des EDP (qqsoit le champ d'application).
-   Analyse fonctionnelle et EDP.
-   Transformée de Fourier.
-   Méthodes numériques.
-   Résolution des grands systèmes linéaires, valeurs propres.
-   Résolution d'équations différentielles.
-   Interpolation, approximation, intégration numérique.


<a id="orgf936121"></a>

## Objectif principal

Mettre en oeuvre **sans se casser la tête** les méthodes ci-dessus pour résoudre
des problèmes numériquement complexe sur des ordinateurs dédiés au calcul,
éventuellement en utilisant les resources de manière optimale.

Ça demande l'utilisation d'outils informatique et numériques spécifiques.


<a id="org357a5bb"></a>

## Liens

Liste de quelques liens.

-   **matlab:** <http://fr.mathworks.com/>, licence commerciale
-   **scilab:** <http://www.scilab.org/fr>, licence open source CeCILL, téléchargeable
    gratuitement
-   **octave:** <https://www.gnu.org/software/octave/>, licence GNU General Public
    License
-   **freefem++:** <http://www.freefem.org/>, licence ??
-   **python:** <https://www.python.org/>, licence PSF (compatible GPL), langage de
    programation généraliste simplet et de haut niveau.
-   **scipy scientific computing stack:** <https://www.scipy.org/about.html>, licences libres variées
-   **julia:** <https://julialang.org/>, nouveau langage dédié au calcul
    scientifique.


<a id="org633bc93"></a>

# Python et les modules scientifiques


<a id="org707cb8e"></a>

## Généralités

-   **Python:** langage de haut niveau, simple et élégant. Python est plus qu'un
    langage de programmation. C'est l'environnement de travail qui permet
    l'exécution du code.
-   **Détails techniques:** typage dynamique, gestion automatique de la mémoire,
    interpreté.
-   **Avantages:** programmation facile, développement rapide, modularité et autres
    bonnes pratiques, beaucoup de bibliothèques dans tous les domaines
-   **Inconvénients:** exécution décentralisée, lente, démarrage peut être difficile


<a id="org12f2e4f"></a>

## Python pour le calcul scientifique

Communauté importante d'utilisateurs, écosystème étendu:

-   **numpy:** <http://numpy.scipy.org> &#x2013; gestion efficace des grands tableaux dans
    python.
-   **scipy:** <http://www.scipy.org> &#x2013; nombreux algorithmes de calculs scientifique,
    organisé en modules, comme algèbre linéaire, transformé de Fourier, etc.
-   **matplotlib:** <http://www.matplotlib.org> &#x2013; sorties graphiques.
-   **mpi4py:** <http://pythonhosted.org/mpi4py> &#x2013; bibliothèque de passage de
    messages entre process pour le calcul parallèle
-   **etc:** et plein d'autres

Bonnes performances grâce à l'integration des bibliothèques optimisées venant du
C ou du Fortran (blas, atlas blas, lapack, arpack, Intel MKL&#x2026;).  Support assez
bon pour le calcul parralèle (threads, openmp, mpi, cuda, opencl)

-   **Schéma de principe:** Python <- Numpy <- {Scipy, Matplotlib, Autres boîtes à
    outils} <- Programme utilisateur

**Note:** Nous utiliserons python pour faire de la programmation
procédurale, et sans utiliser de notions de programmation orientée
objet.


<a id="orgcb1ece7"></a>

## Interpéteur

-   **python:** intepréteur par défaut, lit et exécute un code
    python. Alternativement propose un environnement d'interprétation rustique.
-   **ipython:** interpéteur beaucoup plus riche et commode à utiliser. Avec
    historique des commandes, complétion automatique, édition de code,
    extraction de documentation, interaction avec l'environnement, etc.
-   **jupyter notebook:** environnement de travail augmenté avec possibilité de
    prendre des notes et de montrer des résultats. Nécessite d'utiliser un
    serveur jupyter, édition hors-ligne délicate.


<a id="org4087549"></a>

## Disponibilité, installation

Python est disponible sous linux, windows et MacOS. Dans tous les cas, il faut
installer au minimum: python, ipython, numpy, scipy, matplotlib.

