# FreeCAD-Update-Checker

Macro qui permet d'installer un module de vérification des mises à jour de FreeCAD.

Executer cette macro va installer le module dans le dossier utilisateur. Un nouveau bouton sera installer dans la barre d'outil.
Il est possible d'installer un pack de langues en cochant la case lors de l'installation. (FR, DE, ES, PO), le fichier lang.ts est disponible sur le github si vous souhaitez ajouter ou corriger des traductions.

Une fois installer il est nécessaire de redémarrer FreeCAD ensuite ce module se lancera au démarrage de FreeCAD et vérifiera la présence d'une nouvelle version de FreeCAD à chaque démarrage.

FreeCAD Update checker gère la version stable et la version build hebdomadaire de FreeCAD.

En cas de présence d'une mise à jour disponible, l'icone changera dans la barre d'outil et une tooltip/popup s'affichera quelques instant.
En cliquant sur le bouton vous accedez à la liste des dernières versions stable et developpement disponibles.
Un bouton de téléchargement pour chaque version vous permet d'ouvrir la fenêtre de téléchargement de votre navigateur par défaut.

Afin d'éviter de saturer l'API Github, les données sont mises en cache et vérifiées au maximum 1 fois par heure. Il est possible de forcer la mise à jour en cliquant sur le bouton "Update".

En cas d'absence de connexion internet ou de problèmes de liaisons avec le serveur github l'icone passera en triangle jaune :

En cas de version non prise en charge par FreeCAD Update checker l'icone passe en poitn d'interrogation noire :
