# Projet Flask "Hello, World!"

## Description

Ce projet est une application web Python simple construite avec Flask. Lorsqu'on accède à l'application via un navigateur web, elle affiche "Hello, World!".

## Installation

### Prérequis

- Python 3.x
- pip (Gestionnaire de paquets Python)

### Étapes d'installation

1. **Installez les dépendances** :
    ```bash
    pip install -r requirements.txt
    ```
    *Assurez-vous que le fichier `requirements.txt` est à la racine de votre projet et contient `Flask==<version>`.*

2. **Définissez la variable d'environnement FLASK_APP** :
    - Sur Windows :
      ```cmd
      set FLASK_APP=main.py
      ```
    - Sur macOS et Linux :
      ```bash
      export FLASK_APP=main.py
      ```
    *Remplacez `main.py` par le nom de votre fichier principal si nécessaire.*

3. **Lancez l'application Flask** :
    ```bash
    flask run
    ```
    Après cette commande, vous devriez voir une sortie indiquant l'URL à laquelle l'application est en cours d'exécution (généralement `http://127.0.0.1:5000/`).

4. **Ouvrez cette URL dans votre navigateur web** pour voir le message "Hello, World!".

## Utilisation

Ouvrez votre navigateur web et accédez à l'URL où votre application Flask est en cours d'exécution (normalement `http://127.0.0.1:5000/`) pour voir le message "Hello, World!".

Ajoutez votre prénom à la suite de l'url pour avoir une surprise !

## Contribution

...