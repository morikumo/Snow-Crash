# Level 01

## Indice

Pour ce niveau, nous devons trouver un fichier contenant le mot `flag01`.

## Étapes

1. **Rechercher le fichier contenant `flag01` :**

   Nous avons d'abord essayé de trouver des fichiers appartenant à `flag01`, mais sans succès. Ensuite, nous avons décidé de chercher des fichiers contenant le mot `flag01` à l'intérieur.

   ```bash
   level01@SnowCrash:~$ find / -type f -exec grep -l "flag01" {} \; 2>/dev/null
   ```

   Cette commande trouve tous les fichiers qui contiennent `flag01`. Nous avons trouvé deux fichiers pertinents :
   
   ```bash
   /etc/group
   /etc/passwd
   ```

2. **Analyser les fichiers trouvés :**

   - **/etc/group :** Ce fichier ne contenait rien d'utile pour nous.
   - **/etc/passwd :** Ce fichier contenait des informations intéressantes, notamment des données pour `flag01`.

   En regardant dans le fichier `/etc/passwd`, nous avons trouvé une ligne qui contient un mot de passe hashé pour `flag01` :

   ```bash
   flag00:x:3000:3000::/home/flag/flag00:/bin/bash
   flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
   flag02:x:3002:3002::/home/flag/flag02:/bin/bash
   flag03:x:3003:3003::/home/flag/flag03:/bin/bash
   flag04:x:3004:3004::/home/flag/flag04:/bin/bash
   flag05:x:3005:3005::/home/flag/flag05:/bin/bash
   flag06:x:3006:3006::/home/flag/flag06:/bin/bash
   flag07:x:3007:3007::/home/flag/flag07:/bin/bash
   flag08:x:3008:3008::/home/flag/flag08:/bin/bash
   flag09:x:3009:3009::/home/flag/flag09:/bin/bash
   flag10:x:3010:3010::/home/flag/flag10:/bin/bash
   flag11:x:3011:3011::/home/flag/flag11:/bin/bash
   flag12:x:3012:3012::/home/flag/flag12:/bin/bash
   flag13:x:3013:3013::/home/flag/flag13:/bin/bash
   flag14:x:3014:3014::/home/flag/flag14:/bin/bash
   ```

3. **Décrypter le mot de passe :**

   Le mot de passe trouvé était hashé. Nous avons utilisé `john` pour le décrypter. Voici comment nous avons procédé :

   - Nous avons extrait le hash du fichier `/etc/passwd`.
   - On va sur la machine local pour utiliser john.
   - Nous avons utilisé `john` pour décrypter le hash.

   ```bash
   level01@SnowCrash:~$ john --show hash.txt
   ```

   Après avoir exécuté `john`, nous avons obtenu le mot de passe : `abcdefg`.

## Conclusion

Le mot de passe pour `flag01` est `abcdefg`.

## Résumé

- Nous avons utilisé `find` pour localiser des fichiers contenant `flag01`.
- Nous avons trouvé les fichiers `/etc/group` et `/etc/passwd`.
- Le fichier `/etc/passwd` contenait un hash pour `flag01`.
- Nous avons utilisé `john` pour décrypter le hash.
- Le mot de passe décrypté est `abcdefg`.

```bash
level01@SnowCrash:~$ find / -type f -exec grep -l "flag01" {} \; 2>/dev/null
/etc/passwd
level01@SnowCrash:~$ john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
abcdefg
```

Le mot de passe pour `flag01` est `abcdefg`.
