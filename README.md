# FCUpdate
A macro that installs a module to check for FreeCAD updates.

Running this macro will install the module into the user directory.
A new menu will be added to FreeCAD's menu bar.

![Capture d’écran (31)](https://github.com/user-attachments/assets/95aebf76-52bd-4a31-acd0-26527f3898e9)

You can choose to install the languages pack during installation by checking the box. (FR, DE, ES, PL)
(The lang.ts file is available on GitHub if you want to add or correct translations.)

![Capture d’écran (28)](https://github.com/user-attachments/assets/1429b890-0491-4ccc-ab21-6226fe98095b)

Once installed, you need to restart FreeCAD. After that, the module will automatically launch at startup and check for new FreeCAD versions each time FreeCAD starts.
FCUpdate supports both the stable release and the weekly development builds of FreeCAD.

If an update is available, an icon will appear in the menu bar:

![Capture d’écran (35)](https://github.com/user-attachments/assets/8b68f260-720c-4a87-bb3b-fccedbb8bac9)

The FCUpdate menu gives you access to the list of available files for the latest stable and development versions:

![Capture d’écran (36)](https://github.com/user-attachments/assets/468c5500-4d5f-4094-aa88-af28d5961269)

You can filter the results based on your operating system:

![Capture d’écran (37)](https://github.com/user-attachments/assets/251e7f68-fe88-4410-a3e5-383d5d8dbb45)


Each version includes a download button that opens the download link in your default browser.

Note: To avoid overloading the GitHub API, data is cached and only checked once per hour.
You can force a refresh by clicking the “Reload” button.


------------------------------
# FCUpdate (French)

Macro qui permet d'installer un module de vérification des mises à jour de FreeCAD.

Executer cette macro va installer le module dans le dossier utilisateur. 
Un nouveau menu sera crée dans la barre de menu de FreeCAD

Il est possible d'installer un pack de langues en cochant la case lors de l'installation. (FR, DE, ES, PL).
(Le fichier lang.ts est disponible sur le github si vous souhaitez ajouter ou corriger des traductions.)

Une fois installé, il est nécessaire de redémarrer FreeCAD, ensuite ce module se lancera au démarrage de FreeCAD et vérifiera la présence d'une nouvelle version de FreeCAD à chaque démarrage.
FCUpdate gère la version stable et la version build hebdomadaire de FreeCAD.

En cas de présence d'une mise à jour disponible, une icone apparaitra dans la barre de menu:

Le menu FCUpdate vous permet d'acceder à la liste des fichiers des dernières versions stable et de développement disponibles.

Vous pouvez filtrer les résultats, selon votre système d'exploitation :
Un bouton de téléchargement pour chaque version vous permet d'ouvrir la fenêtre de téléchargement de votre navigateur par défaut.

Information : Afin d'éviter de saturer l'API Github, les données sont mises en cache et vérifiées au maximum 1 fois par heure. 
Il est possible de forcer la mise à jour en cliquant sur le bouton "Reload".

