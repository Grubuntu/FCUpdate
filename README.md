# FreeCAD-Update-Checker

Macro qui permet d'installer un module de vérification des mises à jour de FreeCAD.

Executer cette macro va installer le module dans le dossier utilisateur. 
Un nouveau menu sera crée dans la barre de menu de FreeCAD

![Capture d’écran (31)](https://github.com/user-attachments/assets/95aebf76-52bd-4a31-acd0-26527f3898e9)

Il est possible d'installer un pack de langues en cochant la case lors de l'installation. (FR, DE, ES, PL).
(Le fichier lang.ts est disponible sur le github si vous souhaitez ajouter ou corriger des traductions.)

![Capture d’écran (28)](https://github.com/user-attachments/assets/1429b890-0491-4ccc-ab21-6226fe98095b)

Une fois installé, il est nécessaire de redémarrer FreeCAD, ensuite ce module se lancera au démarrage de FreeCAD et vérifiera la présence d'une nouvelle version de FreeCAD à chaque démarrage.
FCUpdate gère la version stable et la version build hebdomadaire de FreeCAD.

En cas de présence d'une mise à jour disponible, une icone apparaitra dans la barre de menu:

![Capture d’écran (35)](https://github.com/user-attachments/assets/8b68f260-720c-4a87-bb3b-fccedbb8bac9)

Le menu FCUpdate vous permet d'acceder à la liste des fichiers des dernières versions stable et de développement disponibles.
![Capture d’écran (36)](https://github.com/user-attachments/assets/468c5500-4d5f-4094-aa88-af28d5961269)

Vous pouvez filtrer les résultats, selon votre système d'exploitation :
![Capture d’écran (37)](https://github.com/user-attachments/assets/251e7f68-fe88-4410-a3e5-383d5d8dbb45)

Un bouton de téléchargement pour chaque version vous permet d'ouvrir la fenêtre de téléchargement de votre navigateur par défaut.

Information : Afin d'éviter de saturer l'API Github, les données sont mises en cache et vérifiées au maximum 1 fois par heure. 
Il est possible de forcer la mise à jour en cliquant sur le bouton "Reload".

