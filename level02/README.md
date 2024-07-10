# Level 02

## Indice

Pour ce niveau, nous avons un fichier `pcap` qui est une interface de programmation permettant de capturer du trafic réseau.

## Étapes

1. **Identifier le fichier `pcap` :**

   Le fichier `pcap` est directement présent dans le répertoire home de l'utilisateur level02.

   ```bash
   level02@SnowCrash:~$ ls
   level02.pcap
   ```

2. **Copier le fichier pour analyse locale :**

   Pour analyser le fichier plus confortablement, nous le copions sur notre machine locale.

   ```bash
   scp -P 4242 level02@localhost:~/level02.pcap .
   ```

3. **Analyser le fichier `pcap` avec `tshark` :**

   `tshark` est l'outil le plus couramment utilisé pour analyser les fichiers `pcap`. Voici quelques options utiles de `tshark` :

   ```bash
   tshark [ -i <capture interface>|- ] [ -f <capture filter> ] [ -2 ] [ -r <infile> ] [ -w <outfile>|- ] [ options ] [ <filter> ]
   ```

   Pour un premier aperçu du contenu du fichier, nous utilisons :

   ```bash
   tshark -r level02.pcap -Y 'tcp'
   ```

   **Exemple de sortie :**
   ```
     1   0.000000 59.233.235.218 → 59.233.235.223 TCP 74 39247 → 12121 [SYN] Seq=0 Win=14600 Len=0 MSS=1460 SACK_PERM=1 TSval=18592800 TSecr=0 WS=128
     2   0.000128 59.233.235.223 → 59.233.235.218 TCP 74 12121 → 39247 [SYN, ACK] Seq=0 Ack=1 Win=14480 Len=0 MSS=1460 SACK_PERM=1 TSval=46280417 TSecr=18592800 WS=32
     ...
   ```

4. **Filtrer et extraire les données intéressantes :**

   Nous cherchons à extraire des informations utiles. En ciblant le protocole TCP avec `tshark`, nous obtenons une sortie plus compréhensible.

   ```bash
   tshark -r level02.pcap -Y 'tcp' -T fields -e tcp.payload
   ```

   `-T fields` définit le format de sortie et `-e tcp.payload` extrait la charge utile TCP en hexadécimal.

   **Exemple de sortie :**
   ```
   6c
   7f
   4c
   30
   ...
   000d0a4c6f67696e20696e636f72726563740d0a77777762756773206c6f67696e3a20
   ```

5. **Décoder les données hexadécimales :**

   Pour interpréter les données hexadécimales, nous avons deux options :

   - **Option 1 : Utiliser un site de décodage comme dcode.fr.**
   - **Option 2 : Utiliser la commande `xxd` pour convertir les données.**

   **Option 1 : Site de décodage (dcode.fr)**
   ```
   Sortie exemple :
   ÿý%ÿü%ÿû&ÿý�ÿý ÿý#ÿý'ÿý$ÿþ&ÿû�ÿû ÿû#ÿû'ÿü$ÿú �ÿðÿú#�ÿðÿú'�ÿðÿú��ÿðÿú �38400,38400ÿðÿú#�SodaCan:0ÿðÿú'��DISPLAY�SodaCan:0ÿðÿú��xtermÿðÿû�ÿý�ÿý"ÿý�ÿû�ÿý!ÿý�ÿü�ÿû"ÿú"�����b��������b���� B�
   ...
   wwwbugs login: l�le�ev�ve�el�lX�X
   Password: ft_wandr���NDRel�L0L
   ...
   ```

   **Option 2 : Utiliser `xxd`**
   
   Créer un fichier contenant la sortie précédente :

   ```bash
   echo "6c7f4c307f4c0d0a000d0a4c6f67696e20696e636f72726563740d0a77777762756773206c6f67696e3a20" > to_decode.txt
   ```

   Puis, utiliser `xxd` pour décoder :

   ```bash
   xxd -r -p to_decode.txt
   ```

   **Sortie exemple :**
   ```
   ...
   Linux 2.6.38-8-generic-pae (::ffff:10.1.1.2) (pts/10)

   wwwbugs login: lleevveellXX
   Password: ft_wandrNDRelL0L
   ...
   ```

6. **Identifier et nettoyer le mot de passe :**

   Avec l'outil Wireshark on peut voir des "." dans le mots `ft_wandr...NDRel.L0L` .

   Les points on une valeur de `7f` dans le man ascii ça représente : `127   7F    DEL`.

   DEL étant la suppression on supprime directement a partir des points, on va nettoyer tout ça.

   **Mot de passe : `ft_waNDReL0L`**

   **Essayer le mot de passe :**

   ```bash
   su flag02
   password: ft_waNDReL0L
   ```

   **Conclusion :**

   Le mot de passe fonctionne et nous avons réussi à accéder au niveau suivant.

## Résumé

1. Copier le fichier `pcap` pour analyse locale.
2. Utiliser `tshark` pour extraire les données TCP.
3. Décoder les données hexadécimales.
4. Nettoyer et identifier le mot de passe correct.
5. Utiliser le mot de passe pour accéder au niveau suivant.

Le mot de passe pour `flag02` est `ft_waNDReL0L`.
