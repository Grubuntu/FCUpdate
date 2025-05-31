# FreeCAD-Update-Checker

Macro qui permet d'installer un module de vérification des mises à jour de FreeCAD.

Executer cette macro va installer le module dans le dossier utilisateur. 
Un nouveau bouton sera installé dans la barre d'outil.

![Capture d’écran (24)](https://github.com/user-attachments/assets/19dded38-f26b-4be2-bc81-37dfb2c769b7)

Il est possible d'installer un pack de langues en cochant la case lors de l'installation. (FR, DE, ES, PO).
(Le fichier lang.ts est disponible sur le github si vous souhaitez ajouter ou corriger des traductions.)

![Capture d’écran (28)](https://github.com/user-attachments/assets/1429b890-0491-4ccc-ab21-6226fe98095b)

Une fois installé, il est nécessaire de redémarrer FreeCAD, ensuite ce module se lancera au démarrage de FreeCAD et vérifiera la présence d'une nouvelle version de FreeCAD à chaque démarrage.
FreeCAD Update checker gère la version stable et la version build hebdomadaire de FreeCAD.

En cas de présence d'une mise à jour disponible, l'icone changera dans la barre d'outil et une tooltip/popup s'affichera quelques instants.

![Capture d’écran (26)](https://github.com/user-attachments/assets/c325a9df-5ebd-44d2-a2be-94cd33aab3da)

En cliquant sur le bouton de FreeCAD Update Checker vous accedez à la liste des fichiers des dernières versions stable et de developpement disponibles.
Un bouton de téléchargement pour chaque version vous permet d'ouvrir la fenêtre de téléchargement de votre navigateur par défaut.

![Capture d’écran (23)](https://github.com/user-attachments/assets/b678a0ad-dc5c-47f0-b26a-abe199977bbc)


Afin d'éviter de saturer l'API Github, les données sont mises en cache et vérifiées au maximum 1 fois par heure. 
Il est possible de forcer la mise à jour en cliquant sur le bouton "Reload".

En cas d'absence de connexion internet ou de problèmes de liaisons avec le serveur github l'icone passera en triangle jaune :

![Capture d’écran (27)](https://github.com/user-attachments/assets/811287a5-4720-406e-b474-d9d33de4650e)

En cas de version non prise en charge par FreeCAD Update checker l'icone passe en point d'interrogation noire :

