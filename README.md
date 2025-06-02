# FreeCAD-Update-Checker

Macro qui permet d'installer un module de vérification des mises à jour de FreeCAD.

Executer cette macro va installer le module dans le dossier utilisateur. 
Un nouveau menu sera installé dans la barre de menu de FreeCAD

![Capture d’écran (31)](https://github.com/user-attachments/assets/95aebf76-52bd-4a31-acd0-26527f3898e9)

Il est possible d'installer un pack de langues en cochant la case lors de l'installation. (FR, DE, ES, PO).
(Le fichier lang.ts est disponible sur le github si vous souhaitez ajouter ou corriger des traductions.)

![Capture d’écran (28)](https://github.com/user-attachments/assets/1429b890-0491-4ccc-ab21-6226fe98095b)

Une fois installé, il est nécessaire de redémarrer FreeCAD, ensuite ce module se lancera au démarrage de FreeCAD et vérifiera la présence d'une nouvelle version de FreeCAD à chaque démarrage.
FreeCAD Update checker gère la version stable et la version build hebdomadaire de FreeCAD.

En cas de présence d'une mise à jour disponible, l'icone changera dans la barre d'outil et une tooltip/popup s'affichera quelques instants.

![Capture d’écran (34)](https://github.com/user-attachments/assets/722941bc-7240-438a-a7da-77dab33156d8)


Le menu FCUpdate vous permet d'acceder à la liste des fichiers des dernières versions stable et de developpement disponibles.
Un bouton de téléchargement pour chaque version vous permet d'ouvrir la fenêtre de téléchargement de votre navigateur par défaut.

![Capture d’écran (23)](https://github.com/user-attachments/assets/b678a0ad-dc5c-47f0-b26a-abe199977bbc)

Information : Afin d'éviter de saturer l'API Github, les données sont mises en cache et vérifiées au maximum 1 fois par heure. 
Il est possible de forcer la mise à jour en cliquant sur le bouton "Reload".

