Voici le README détaillé pour le niveau 14, incluant toutes les étapes et explications nécessaires :

---

# Level 14

## Contexte

Arrivés au niveau 14, nous n'avons absolument rien dans notre répertoire personnel. Pour progresser, nous devons utiliser une approche de reverse engineering sur l'exécutable `getflag`.

## Étapes

### 1. Identifier l'exécutable `getflag`

Pour commencer, nous devons localiser l'exécutable `getflag` qui est utilisé pour obtenir les flags dans les niveaux précédents.

```bash
level14@SnowCrash:~$ which getflag
/bin/getflag
```

### 2. Transférer l'exécutable pour analyse locale

Une fois l'exécutable localisé, nous le transférons sur notre machine locale pour une analyse approfondie. Nous pouvons utiliser `scp` pour ce faire :

```bash
scp level14@<IP>:<PATH_TO_GETFLAG> ./getflag
```

### 3. Analyse de l'exécutable avec un décompilateur

Utilisez Ghidra ou un autre décompilateur pour analyser le binaire. Nous découvrons une grande condition composée de 15 `else if`, correspondant aux 15 niveaux. Le dernier `else if` contient la condition pour notre niveau (UID 3014) avec un message crypté.

### 4. Décryptage et conditions

Nous observons une fonction `ft_des` qui décrypte les messages. Malheureusement, tenter de décrypter directement échoue. Nous notons cependant l'utilisation de `ptrace` pour détecter le débogage, ce qui nous empêche de déboguer directement.

### 5. Analyse avec GDB

Nous utilisons GDB pour continuer notre analyse et récupérer le flag.

```bash
level14@SnowCrash:~$ gdb getflag
(gdb) b main
(gdb) r
(gdb) disas main
```

La commande `disas main` nous permet de désassembler la fonction main et de comparer avec l'assemblage obtenu dans Ghidra. Cela nous aide à nous repérer et à vérifier que notre analyse est correcte.

### 6. Contourner `ptrace`

Nous plaçons un point d'arrêt juste avant l'appel à `ptrace` pour contourner sa vérification.

```bash
(gdb) b *main+67
(gdb) r
```

L'instruction `ptrace` est utilisée pour empêcher le débogage. En contournant cette vérification, nous évitons que le programme se termine prématurément.

### 7. Sauter directement à la partie intéressante du code

Pour accéder directement au code qui affiche le flag, nous utilisons la commande `jump` pour sauter à l'adresse après les vérifications des UID.

```bash
(gdb) jump *main+1183
```

La commande `jump` modifie le pointeur d'instruction pour sauter directement à l'adresse `main+1183`, contournant ainsi les vérifications et affichant le flag.

### 8. Résultat

En utilisant les étapes ci-dessus, nous obtenons le token pour le niveau 14 :

```bash
7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
```

## Conclusion

En résumé, nous avons utilisé une combinaison d'analyse statique avec Ghidra et d'analyse dynamique avec GDB pour contourner les protections mises en place dans l'exécutable `getflag` et obtenir le flag pour le niveau 14.

---

