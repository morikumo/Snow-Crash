
Le niveau 13 nous présente un binaire exécutable nommé `level13`. 
L'objectif est de comprendre son comportement et de trouver une méthode pour obtenir le jeton (token).

#### Analyse du binaire

Le binaire `level13` lorsqu'il est exécuté affiche le message suivant :

```
UID 2013 started us but we we expect 4242
```

Ce message indique que le programme vérifie l'UID (User ID) de l'utilisateur qui l'exécute et attend que cet UID soit `4242`.

#### Décompilation du binaire

Voici le code décompilé du binaire `level13` :

```c
void main(void)
{
  __uid_t _Var1;
  undefined4 uVar2;

  _Var1 = getuid();
  if (_Var1 != 0x1092) {
    _Var1 = getuid();
    printf("UID %d started us but we we expect %d\n", _Var1, 0x1092);
    exit(1);
  }
  uVar2 = ft_des("boe]!ai0FB@.:|L6l@A?>qJ}I");
  printf("your token is %s\n", uVar2);
  return;
}
```

Le programme vérifie si l'UID est `4242`. Si ce n'est pas le cas, il affiche un message d'erreur et quitte. 
Sinon, il procède à l'appel de la fonction `ft_des` avec une chaîne cryptée, puis affiche le résultat comme étant le jeton.

#### Utilisation de GDB pour contourner la vérification de l'UID

Pour contourner la vérification de l'UID, nous pouvons utiliser GDB (GNU Debugger) pour modifier l'exécution du programme et passer cette vérification. 
Voici les étapes à suivre :

1. **Définir un point d'arrêt à l'entrée de la fonction `main` :**

   ```sh
   gdb -q ./level13
   Reading symbols from /home/user/level13/level13...(no debugging symbols found)...done.
   (gdb) b main
   Breakpoint 1 at 0x804858f
   ```

2. **Exécuter le programme :**

   ```sh
   (gdb) run
   Starting program: /home/user/level13/level13 
   ```

3. **Examiner les instructions autour de `eip` (Instruction Pointer) :**

   ```sh
   (gdb) x/20i $eip
   => 0x804858f <main+3>:	and    $0xfffffff0,%esp
      0x8048592 <main+6>:	sub    $0x10,%esp
      0x8048595 <main+9>:	call   0x8048380 <getuid@plt>
      0x804859a <main+14>:	cmp    $0x1092,%eax
      0x804859f <main+19>:	je     0x80485cb <main+63>
      0x80485a1 <main+21>:	call   0x8048380 <getuid@plt>
      0x80485a6 <main+26>:	mov    $0x80486c8,%edx
      0x80485ab <main+31>:	movl   $0x1092,0x8(%esp)
      0x80485b3 <main+39>:	mov    %eax,0x4(%esp)
      0x80485b7 <main+43>:	mov    %edx,(%esp)
      0x80485ba <main+46>:	call   0x8048360 <printf@plt>
      0x80485bf <main+51>:	movl   $0x1,(%esp)
      0x80485c6 <main+58>:	call   0x80483a0 <exit@plt>
      0x80485cb <main+63>:	movl   $0x80486ef,(%esp)
      0x80485d2 <main+70>:	call   0x8048474 <ft_des>
      0x80485d7 <main+75>:	mov    $0x8048709,%edx
      0x80485dc <main+80>:	mov    %eax,0x4(%esp)
      0x80485e0 <main+84>:	mov    %edx,(%esp)
      0x80485e3 <main+87>:	call   0x8048360 <printf@plt>
      0x80485e8 <main+92>:	leave  
   ```

4. **Définir `eip` à l'adresse après la vérification de l'UID :**

   ```sh
   (gdb) set $eip = 0x80485cb
   ```

5. **Continuer l'exécution pour obtenir le jeton :**

   ```sh
   (gdb) continue
   Continuing.
   your token is 2A31L79asukciNyi8uppkEuSx
   ```

Cette méthode permet de contourner la vérification de l'UID en sautant directement à l'adresse où le jeton est décrypté et affiché.

### Conclusion

En utilisant GDB, nous avons pu contourner la vérification de l'UID et obtenir le jeton requis pour passer au niveau suivant.
Ce processus montre l'importance de comprendre les registres du processeur et comment les utiliser pour manipuler l'exécution du programme.
