# Webradio
Crée ta propre Webradio avec un Raspberry PI (Python 3) !

Ce programme permet de lire des musiques et des jingles de façon automatique.
Fonctionnalité du programme :
- Lire des musiques aléatoires
- Intercaller entre chaque musique un jingle
- Lancer des pubs
- Lancer un TOP Horaire
- Mode autoplay
- Mode Manuel

# Pré-requis
Il faut installer Pygame
```
pip install pygame
```

# Informations et problèmes
⚠ Il faut ajouter les fichier audios (.mp3 / .wav) :
- Les musiques dans le dossier musique
- Les jingles dans le dossier Jingle
- Les pubs dans le dossier pubs
- Le ou les  Top Horaire dans le dossier TOPH

⚠ Il faut supprimer les fichier readme.md dans chaque dossier !

⚠ Sur le programme, il faut changer les 4 prèmières lignes en fonction de vos dossiers, attention a bien mettre "\\" entre chaque dossier.

⚠ Les pubs doivent être renomées en 1.mp3 pour la première et 2.mp3 pour la deuxième

ℹ Le Top Horaire est lancé à chaque xxh00 et les pubs a chaque xxh30
