import sys 

#Expand Python classes path with your app's path
#Emplacement du répertoire à changer en fonction de l'endroit où se situe le dossier du site web
sys.path.insert(0, 'C:/wamp64/www/Phylogenie') 

from app import app as application
