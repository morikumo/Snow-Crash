# Level 09

## Étapes pour résoudre le challenge

### 1. Initialisation

Nous avons deux fichiers : un exécutable `level09` et un fichier `token` dont les droits sont limités. Toutefois, nous pouvons afficher le fichier `token` avec `cat`.

### 2. Affichage du contenu du fichier `token`

```bash
cat token
```

**Sortie :**
```
f4kmm6p|=�p�n��DB�Du{��
```

Le contenu du fichier `token` est illisible.

### 3. Exécution de l'exécutable `level09`

Nous essayons d'exécuter `level09` pour voir son comportement.

```bash
./level09
```

**Sortie :**
```
You need to provide only one arg.
```

L'exécutable attend un argument. Nous essayons de lui donner le fichier `token` comme argument.

```bash
./level09 token
```

**Sortie :**
```
tpmhr
```

Ce résultat n'est pas le mot de passe attendu.

### 4. Analyse de l'exécutable avec `ltrace`

Nous utilisons `ltrace` pour observer les appels système et les bibliothèques utilisées par le programme.

```bash
ltrace ./level09 token
```

**Sortie :**
```
__libc_start_main(0x80487ce, 2, 0xbffff7e4, 0x8048aa0, 0x8048b10 <unfinished ...>
ptrace(0, 0, 1, 0, 0xb7e2fe38) = -1
puts("You should not reverse this"You should not reverse this
) = 28
+++ exited (status 1) +++
```

Le programme affiche "You should not reverse this". Nous allons donc essayer de le reverse.

### 5. Analyse du binaire avec Ghidra

Nous utilisons Ghidra pour analyser le binaire `level09` et nous trouvons la logique de transformation.

**Code :**
```c
putchar((int)*(char *)(local_120 + *(int *)(param_2 + 4)) + local_120);
```

Nous comprenons que le programme effectue une opération sur chaque caractère du fichier `token`.

### 6. Script Python pour inverser la transformation

Nous écrivons un script Python pour inverser cette transformation.

**Script Python :**
```python
import sys

i = -1
content = open("/home/user/level09/token").readlines()[0]
for c in content:
    i += 1
    try:
        sys.stdout.write(chr(ord(c) - i))
    except:
        pass
print("\n")
```

Nous mettons le script dans `/tmp` et l'exécutons.

```bash
vim /tmp/script.py
chmod +x /tmp/script.py
python /tmp/script.py
```

**Sortie :**
```
f3iji1ju5yuevaus41q1afiuq
```

Nous obtenons le flag `f3iji1ju5yuevaus41q1afiuq`.

### 7. Accès au niveau suivant

Nous utilisons le flag pour nous connecter en tant que `flag09`.

```bash
su flag09
password : f3iji1ju5yuevaus41q1afiuq
```

Ensuite, nous exécutons la commande `getflag`.

```bash
getflag
```

**Sortie :**
```
s5cAJpM8ev6XHw998pRWG728z
```

Le flag pour `level09` est : `s5cAJpM8ev6XHw998pRWG728z`.

## Résumé

Pour résoudre ce challenge, nous avons analysé les fichiers disponibles, utilisé `ltrace` pour comprendre les vérifications effectuées par le programme, et exploité les informations obtenues pour inverser la transformation appliquée par le programme à l'aide d'un script Python.

Le flag pour `level09` est : `s5cAJpM8ev6XHw998pRWG728z`.
