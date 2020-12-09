# Site Web sur serveur local WAMP
![Zozor](https://blog.nicolashachet.com/wp-content/uploads/2011/05/wamp.png)


## Installation du logiciel
https://www.wampserver.com/en/download-wampserver-64bits/

## Insatllation package mod_wsgi

Dans un terminal, tapez les commandes suivantes:
1. pip install mod_wsgi
2. mod_wsgi-express install-module
3. Allez dans votre dossier wamp64\bin\apache\apache2.4.46\conf\httpd.conf
4. Copiez les 3 lignes obtenues en point 2 à la suite des "LoadModule" (l'endroit n'a pas d'importance)
5. Ajoutez la ligne WSGIApplicationGroup %{GLOBAL}
6. Sauvegardez et fermez le fichier

## Création du script .wsgi
Le plus pratique est de mettre ce script dans un dossier dédié. Ici, nous l'appelons, scripts_wsgi.

## Configuration du virtual host de Wamp

1. Créez l'environnement depuis la page d'accueil de Wamp (localhost)
2. Allez dans le fichier wamp64\bin\apache\apache2.4.46\conf\extra\httpd-vhosts.conf
3. Modifiez le code de votre virtual host comme ceci (les chemins sont à modifier en fonction de votre configuration) :

![Zozor](https://zupimages.net/up/20/50/4yf2.png)

4. Sauvegardez et fermez le fichier











