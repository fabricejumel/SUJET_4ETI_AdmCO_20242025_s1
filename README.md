## Tamagotchi

![Robot Target](Designer_s.jpg)

Votre rendu sera un unique dépôt Git. Vous devrez définir et justifier l'organisation des branches, l'utilisation ou non de branches `dev`, de branches liées aux fonctionnalités, de branches distinctes pour les versions, ou l'utilisation de tags.


Testez le code [tamagotchi.py](./tamagotchi.py)

Dans le cas où le sujet ne vous paraitrez peu clair ou erroné, proposez des changements en les justifiant pour pouvoir répondre aux questions .
Même si rien ne marche, remplissez au mieux les attendus en étant clair sur ce qui marche et ce qui ne marche pas (cf la suite).

> [!IMPORTANT] 
> Soyez clair dans le README de votre main du rendu principal, où je dois trouver les differentes versions attendues

Pour chaque Version, vous devrez :

1. ***Expliquer ce qui marche et ce qui ne marche pas***
1. ***Joindre des copies d'écran, du résultats des scripts exécutés***
1. **Expliquer l'interet et  l'usage de venv dasn votre cas (rester simple), dans votre cas (NE PAS JOINDRE DE REPERTOIRE Venv dans votre git ou de fichiers temporaires)**
1. **Coder la ou les classes et le package associé et les déposer sur test Pypi** 
1. **Mettre en place des tests, les plus complets possibles en utilisant unitest** : en particulier, comment gérez-vous les éventuelles erreurs ?
1. **Afficher les choix sur le code final de la classe si vous avez dû faire des changements** :  Affichez entre autre votre score et le retour de Pylint lmais surtout expliquer vos choix d'architecture et de code
1. **Associer au projet gitlab le README le plus complet possible**
1. **Faire un gros effort sur les commentaires** : utilisez intensivement les docstrings.
1. **Proposer l'installation du paquet directment à partir de gitlab avec une procedure dans le README**, soyez vigilant à la version
1.  **Proposer l'installation du paquet à partir de test pypi avec une procédure dans le README**,  soyez vigilant à la version
1. **Automatiser les phases de test et de création du .whl sur GitLab avec un fichier ci** 
1. **Faire apparaitre votre arbre de commit dans le README, en expliquant les choix faits sur les branches et les tags**


### Version 1 (8 points + bonus) tag 1.0

Le but est de cette version est de mettre en forme le code donné pour en créer un package (logique setup.py ou éventuellemnt pyproject.toml) en modifiant a le code donné . On mettra en complément  en place toute la logique de test unitaires. On expliquera le code et les test dans le README. Idéallement on séparera le cycle de vie du tamagotchi et les interactions "clavier " que l'on a avec lui. On, rajoutera aussi  le stockage des resultats (nombre d'étape atteintes pour chaque partie (avec la suite d'actions associés) . On pourra faire en sorte que le joueur s'dentifie avec son prenom.
> [!IMPORTANT]
> on relira l'attendu précédent. Pour chaque Version, vous devrez : ...

### Version 2 ( 12 points + des bonus)  tag 2.0

Le code proposé présente beaucoup d'améliorations possibles . En particulier on souhaite développer des stratégies de jeux par ordinateur. On proposera une version où l'ordinateur joue automatiquement en suivant une stratégie. On proposera au moins 2 stratégies que l'on peux chosir avec des arguments dans le code , une stragégie totalement aléatoire  et une stragégie ou l'ordinateur plus interessante. Vous pouvez ensuite si vous le souhaitez proposer d'autres améliorations . 
. Il est important que tous les changements se reperercutent sur les tests unitaires . N'hésitez pas à améliorer/enrichir au passage vos tests unitaires si il n'était pas suffisamment complet sur la version 1. Le README doit donner toutes les informations pertinentes sur le code et les test.



> [!IMPORTANT]
> on relira l'attendu précédent. Pour chaque Version, vous devrez : ...



