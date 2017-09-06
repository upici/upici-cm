<div id="table-of-contents">
<h2>Table des matières</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline6">1. Organisation pratique, évaluation</a>
<ul>
<li><a href="#orgheadline1">1.1. Les objectifs principaux</a></li>
<li><a href="#orgheadline2">1.2. La méthode pour y arriver</a></li>
<li><a href="#orgheadline3">1.3. Outils et resources</a></li>
<li><a href="#orgheadline4">1.4. Évaluation</a></li>
<li><a href="#orgheadline5">1.5. Emploi du temps</a></li>
</ul>
</li>
<li><a href="#orgheadline15">2. Quelques mots sur le calcul scientifique (dans ce cours)</a>
<ul>
<li><a href="#orgheadline7">2.1. Introduction</a></li>
<li><a href="#orgheadline8">2.2. Résoudre des problèmes concret de science ou d'ingénierie (industrie, santé&#x2026;)</a></li>
<li><a href="#orgheadline9">2.3. Des problèmes spécifiques</a></li>
<li><a href="#orgheadline10">2.4. Matériel</a></li>
<li><a href="#orgheadline11">2.5. Outils informatiques</a></li>
<li><a href="#orgheadline12">2.6. Mathématiques</a></li>
<li><a href="#orgheadline13">2.7. Objectif principal</a></li>
<li><a href="#orgheadline14">2.8. Liens</a></li>
</ul>
</li>
</ul>
</div>
</div>


# Organisation pratique, évaluation<a id="orgheadline6"></a>

## Les objectifs principaux<a id="orgheadline1"></a>

-   Découvrir les possibilités d'un langage de haut niveau pour le calcul
    scientifique, dans notre cas Python avec les modules Numpy, Scipy, Matplotlib,
    etc.
-   Découvrir les EDP et leurs approximations par la pratique.

## La méthode pour y arriver<a id="orgheadline2"></a>

Travailler en groupe collaboratifs, en présentiel et à distance: apprentissage
par projets et séances de mise en commun.

Chaque groupe de 3 ou 4 étudiants a en charge la réalisation d'un projet. Le
projet est réalisé pendant les heures de TP et librement en dehors. Chaque
projet donne lieu à

-   un compte rendu hebdomadaire d'avancement;
-   un temps d'échange après quelques séances;
-   la réalisation d'un compte-rendu terminal;
-   un exposé devant l'ensemble des étudiants.

## Outils et resources<a id="orgheadline3"></a>

-   Le langage Python (et les modules cités plus haut), <https://www.python.org>
-   L'outil Git, par l'intermédiaire de la plateforme, <http://github.com>
-   Le langage Markdown, pour l'écriture de compte-rendus hebdomadaires, <https://daringfireball.net/projects/markdown>
-   Le langage Latex, <https://www.latex-project.org>

**Voir plus bas pour avoir trouver des liens pour découvrir ces outils**

## Évaluation<a id="orgheadline4"></a>

-   Session 1 : 0.7\*rapport + 0.3\*contrôle continu (présentation + cr hebdomadiares)
-   Session 2 : 0.7\*2e version du rapport + 0.3\*max(contrôle continu de
    session 1, note rapport session 2), ie règle du max

## Emploi du temps<a id="orgheadline5"></a>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">CM 1</td>
<td class="org-left">mardi 05/09/2017</td>
<td class="org-left">10:00 12:00</td>
<td class="org-left">A13/ Salle 9</td>
</tr>


<tr>
<td class="org-left">TP 1</td>
<td class="org-left">mardi 12/09/2017</td>
<td class="org-left">08:00 11:00</td>
<td class="org-left">A28/ Salle 103 (CREMI)</td>
</tr>


<tr>
<td class="org-left">TP 2</td>
<td class="org-left">mardi 19/09/2017</td>
<td class="org-left">08:00 11:00</td>
<td class="org-left">A28/ Salle 208 (CREMI)</td>
</tr>


<tr>
<td class="org-left">TP 3 (\*)</td>
<td class="org-left">mardi 03/10/2017</td>
<td class="org-left">08:00 11:00</td>
<td class="org-left">A28/ Salle 208 (CREMI)</td>
</tr>


<tr>
<td class="org-left">TP 4</td>
<td class="org-left">mardi 17/10/2017</td>
<td class="org-left">08:00 11:00</td>
<td class="org-left">A28/ Salle 208 (CREMI)</td>
</tr>


<tr>
<td class="org-left">TP 5</td>
<td class="org-left">mardi 14/11/2017</td>
<td class="org-left">08:00 11:00</td>
<td class="org-left">A28/ Salle 208 (CREMI)</td>
</tr>


<tr>
<td class="org-left">TP 6</td>
<td class="org-left">mardi 21/11/2017</td>
<td class="org-left">08:00 11:00</td>
<td class="org-left">A28/ Salle 208 (CREMI)</td>
</tr>


<tr>
<td class="org-left">TP 7</td>
<td class="org-left">mardi 28/11/2017</td>
<td class="org-left">08:00 10:00</td>
<td class="org-left">A28/ Salle 208 (CREMI)</td>
</tr>


<tr>
<td class="org-left">CM 2 (\*)</td>
<td class="org-left">mardi 05/12/2017</td>
<td class="org-left">10:15 12:15</td>
<td class="org-left">A13/ Salle 9</td>
</tr>
</tbody>
</table>

(\*) rapport ou présentation orale

# Quelques mots sur le calcul scientifique (dans ce cours)<a id="orgheadline15"></a>

## Introduction<a id="orgheadline7"></a>

L'objectif est de découvrir quelques environnements de travail qui facilitent le
développement de solutions basée sur le calcul scientifique et l'utilisation de
plateformes de calcul haute performance.

En sciences, le calcul scientifique devient un troisième axe de recherche à côté
de la théorie et de l'expérience. Dans le mon,de professionnel, il devient un
outil à part entière de résolution de problèmes et de conception de solutions
techniques. Il existe désormais plusieurs outils matures qui facilitent et
accélèrent le développement de ces solutions techniques. La maîtrise de ces
outils et du calcul scientifique est un atout important de la recherche
d'emploi.

## Résoudre des problèmes concret de science ou d'ingénierie (industrie, santé&#x2026;)<a id="orgheadline8"></a>

Quelques questions importantes à propos du calcul scientifique:

-   Division théorie et expérimental en science ? Place et rôle du calcul

scientifique ?

-   Quelles plateformes matérielles, quels outils informatiques, quelles méthodes

mathématiques ?

-   Comment assurer la eproductibilité des résultats ? Quelles sont les bonnes
    pratiques de programmation pour cela (gestion de versions &#x2013; git, svn&#x2026; &#x2013;,
    tests, documentation&#x2026;) ?

## Des problèmes spécifiques<a id="orgheadline9"></a>

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

## Matériel<a id="orgheadline10"></a>

-   **Ordinateurs portable:** faibles performances mais très répandus, en général
    multicoeur à mémoire partagée.
-   **Stations de travail fixes:** meilleures performances, multicoeur ou
    multiprocesseur à mémoire partagé.
-   **Serveurs de calcul:** performances importantes à très importantes, nombreuses
    architectures possibles, mais modèles hiérarchique et complexes difficiles
    à programmer.

## Outils informatiques<a id="orgheadline11"></a>

-   **bibliothèques:** qui permettent d'accéder aux fonctionnalités du matériels,
    comme MPI et autres techniques de communication ou gestion de la mémoire et
    de l'exécution (openMP), mais aussi les bibliothèques de calcul matriciel
    (BLAS, LAPACK, UMFPACK, HIPS, MUMPS&#x2026;).
-   **langages de programmation:** Fortran, C, C++, proches de la machine, utilisent
    directement les bibliothèques.
-   **langages de haut niveaux:** sans compilation, avec interface simplifié et
    intuitive avec les bibliothèques, temps de développement raccourci,
    maintien plus simple, interface intuitive avec les bibliothèques&#x2026;

## Mathématiques<a id="orgheadline12"></a>

-   Les problèmes sont souvent du domaine des EDP (qqsoit le champ d'application).
-   Analyse fonctionnelle et EDP.
-   Transformée de Fourier.
-   Méthodes numériques.
-   Résolution des grands systèmes linéaires, valeurs propres.
-   Résolution d'équations différentielles.
-   Interpolation, approximation, intégration numérique.

## Objectif principal<a id="orgheadline13"></a>

Mettre en oeuvre **sans se casser la tête** les méthodes ci-dessus pour résoudre
des problèmes numériquement complexe sur des ordinateurs dédiés au calcul,
éventuellement en utilisant les resources de manière optimale.

Ça demande l'utilisation d'outils informatique et numériques spécifiques.

## Liens<a id="orgheadline14"></a>

Liste de quelques pointeurs pour le calcul scientifique

-   **matlab:** <http://fr.mathworks.com/>, licence commerciale
-   **scilab:** <http://www.scilab.org/fr>, licence open source CeCILL, téléchargeable
    gratuitement
-   **octave:** <https://www.gnu.org/software/octave/>, licence GNU General Public
    License
-   **freefem++:** <http://www.freefem.org/>, licence ??
-   **python:** <https://www.python.org/>, licence PSF (compatible GPL), langage de
    programation généraliste simplet et de haut niveau.
-   **scipy scientific computing stack:** <https://www.scipy.org/about.html>, licences libres variées
