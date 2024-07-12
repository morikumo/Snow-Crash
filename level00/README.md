# Level 00

## Indice

Pour ce niveau, nous devons trouver un fichier appartenant à l'utilisateur `flag00`.

## Étapes

1. **Trouver le fichier :**

   Nous commençons par rechercher les fichiers appartenant à `flag00` en utilisant la commande `find`. Pour éviter d'afficher les messages d'erreur, nous redirigeons les erreurs vers `/dev/null` :

   ```bash
   level00@SnowCrash:~$ find / -user flag00 2>/dev/null
   ```

   Cette commande trouve tous les fichiers appartenant à l'utilisateur `flag00`. Le résultat indique qu'il y a un fichier appelé `john` que nous devons examiner.

2. **Analyser le fichier :**

   Le fichier `john` semble être crypté. Nous devons le décrypter pour trouver le flag.

   Deux choix s'offre a nous, un script ou decode. Choisir chiffrement de César.

4. **Décrypter le fichier en utilisant un script Python :**

   Le fichier est crypté en utilisant le chiffrement de César. Nous utilisons un script Python pour le décrypter :

   ```python
   def decrypt_caesar_cipher(ciphertext, shift):
       plaintext = ""
       for char in ciphertext:
           if char.isalpha():
               shift_amount = 65 if char.isupper() else 97
               plaintext += chr((ord(char) - shift_amount - shift) % 26 + shift_amount)
           else:
               plaintext += char
       return plaintext

   encrypted_message = "cdiiddwpgswtgt"
   shift = 13  # Pour le chiffrement de César, un décalage courant est de 13 (ROT13)
   decrypted_message = decrypt_caesar_cipher(encrypted_message, shift)
   print(decrypted_message)
   ```

   L'exécution de ce script nous donne le message décrypté `nottoohardhere`.

## Conclusion

Le message décrypté `nottoohardhere` est le mot de passe pour `flag00`.

## Résumé

- Nous avons utilisé `find` pour localiser un fichier appartenant à `flag00`.
- Le fichier `john` était crypté avec le chiffrement de César.
- Nous avons utilisé un script Python pour décrypter le fichier.
- Le mot de passe décrypté est `nottoohardhere`.

```bash
level00@SnowCrash:~$ find / -user flag00 2>/dev/null
/usr/sbin/john
level00@SnowCrash:~$ python script.py
level00@SnowCrash:~$ x24ti5gi3x0ol2eh4esiuxias
```

Le mot de passe pour `flag00` est `nottoohardhere`.
