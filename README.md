## [Towers of Hanoi](https://cses.fi/problemset/task/2165)

### A játék leírása

A Hanoi tornyai játék három oszlopból (bal, középső és jobb) és n darab, különböző méretű kerek korongból áll. Kezdetben az összes korong a bal oldali oszlopban helyezkedik el, növekvő sorrendben a tetejétől az aljáig.

**Cél:** Az összes korongot át kell mozgatni a jobb oldali oszlopba a következő szabályok betartásával:
1. Egy lépésben mindig csak a legfelső korong mozgatható egyik oszlopból egy másikba.
2. Egyik oszlopban sem lehet egy nagyobb korongot egy kisebb korong tetejére helyezni.

### Feladat

A játék célja olyan lépéssorozat megtalálása, amely minimális számú mozdulattal oldja meg a problémát.

**Bemenet:**
- Egyetlen egész szám, n, amely a korongok számát adja meg.

**Kimenet:**
1. Egy egész szám, k, amely a minimális mozgások számát jelzi.
2. k darab sor, amelyek mindegyike két egész számot tartalmaz, a és b, ahol a-ból b-be mozgat egy korongot.

**Korlátok:**

$$1 \leq n \leq 16$$

### Algoritmus magyarázata

A feladat megoldására a következő rekurzív algoritmust alkalmazza:

1. **Báziseset:**
   - Ha csak egy korong van (\(n=1\)), azt közvetlenül a bal oszlopból a jobb oszlopba mozgatja.

2. **Rekurzív eset:**
   - Az \(n-1\) darab legfelső korongot átmozgatja a középső oszlopba, miközben a jobb oszlopot használja segédoszlopként.
   - Ezután az \(n\)-edik (legnagyobb) korongot a bal oszlopból a jobb oszlopba helyezi.
   - Végül az \(n-1\) korongot átrakja a középső oszlopból a jobb oszlopba, miközben a bal oszlop lesz a segédoszlop.

#### Minimális lépések száma:
A lépések száma rekurzívan számolható a következő képlettel:

$$k = 2^n - 1$$

---

## [Sliding Window Medion](https://cses.fi/problemset/task/2165)

### A probléma leírása

Adott egy \(n\) egész számot tartalmazó tömb. A feladat, hogy minden \(k\)-elemű csúszó ablakra kiszámítsa a mediánt balról jobbra haladva.

**Medián:** A medián a sorba rendezett elemek középső értéke. Ha a sorba rendezett elemek száma páros, akkor a két középső érték közül a kisebbet tekintjük mediánnak.

### Feladat

**Bemenet:**
- Az első sor két egész számot tartalmaz: \(n\) (az elemek száma) és \(k\) (az ablak mérete).
- A második sor tartalmazza az \(n\) számot, \(x_1, x_2, \ldots, x_n\): a tömb elemei.

**Kimenet:**
- \(n-k+1\) számot kell kiírni, amelyek az ablakonkénti mediánokat jelentik.

**Korlátok:**
- $$1 \leq k \leq n \leq 2 \cdot 10^5$$
- $$1 \leq x_i \leq 10^9$$

### Példa

**Bemenet:**
```
8 3
2 4 3 5 8 1 2 1
```

**Kimenet:**
```
3 4 5 5 2 1
```

### Algoritmus magyarázata

1. **Adatszerkezet használata:** A medián hatékony kiszámításához rendezett adatszerkezetre van szükség, amely támogatja az elemek beszúrását, törlését és a középső elem gyors kiválasztását (pl. két halmot használhatunk).

2. **Ablak mozgatása:** Az \(i\)-edik ablak mediánját a következőképpen számítja:
   - Adja hozzá az ablak új elemét.
   - Törölje az ablakból kikerülő elemet.
   - A halmok segítségével számítsa ki a mediánt.

3. **Időbeli hatékonyság:** Az algoritmus időbonyolultsága \(O(n \log k)\), mivel minden ablakelem beszúrása és törlése \(O(\log k)\), és az ablak mérete \(n-k+1\).

## [Counting Numbers](https://cses.fi/problemset/task/2220)

### A probléma leírása

A feladat olyan egész számok megszámlálása, amelyekben nincs két egymás melletti azonos számjegy, egy adott **a** és **b** közötti intervallumban (beleértve **a**-t és **b**-t is).

### Feladat

**Bemenet:**
- Egyetlen sor, amely két egész számot tartalmaz: a és b

**Kimenet:**
- Egy egész szám: azon számok mennyisége az $$[a,b]$$ intervallumban, amelyekben nincs két egymás melletti azonos számjegy.

**Korlátok:**
- $$0 \leq a \leq b \leq 10^{18}$$

### Példa

**Bemenet:**
```
123 321
```

**Kimenet:**
```
171
```

### Algoritmus magyarázata

1. **Dinamikus programozás:** A feladat megoldásához érdemes dinamikus programozást alkalmazni, mivel a számok nagy tartományban mozoghatnak.

2. **Állapotok:** Az állapotokat úgy definiálhatjuk, hogy figyelembe vesszük az aktuális számjegyet és az előző számjegyet.

3. **Átmenetek:** Az átmeneteknél figyelnünk kell arra, hogy ne legyen két egymás melletti azonos számjegy.

4. **Határesetek kezelése:** Külön kell kezelni az **a** és **b** határeseteket, hogy pontosan az $$[a,b]$$ intervallumba eső számokat számoljuk.

5. **Időbeli hatékonyság:** Az algoritmus időbonyolultsága $$O(\log b)$$, mivel a számjegyek számával arányos a futásidő.


## [Teleporters Path](https://cses.fi/problemset/task/1693)

### A probléma leírása

Egy játékban n szint és m teleportáló van. A játékot akkor nyered meg, ha az 1. szintről eljutsz az n. szintre úgy, hogy minden teleportálót pontosan egyszer használsz.

### Feladat

Meg kell határozni, hogy lehetséges-e megnyerni a játékot, és ha igen, mi egy lehetséges útvonal.

**Bemenet:**
- Az első sor két egész számot tartalmaz: n (szintek száma) és m (teleportálók száma). A szintek 1,2,...,n számozásúak.
- Ezután m sor következik, amelyek a teleportálókat írják le. Minden sor két egész számot tartalmaz, a és b: van egy teleportáló az a szintről a b szintre.
- Feltételezhetjük, hogy minden (a,b) pár különböző a bemenetben.

**Kimenet:**
- m+1 egész szám: a szintek sorrendje, ahogy a játék során meglátogatod őket. Bármely érvényes megoldást kinyomtathatod.
- Ha nincs megoldás, írd ki, hogy "IMPOSSIBLE".

**Korlátok:**
- $$2 \le n \le 10^5$$
- $$1 \le m \le 2 \cdot 10^5$$
- $$1 \le a,b \le n$$

### Példa

**Bemenet:**

**Bemenet:**
```
5 6
1 2
1 3
2 4
2 5
3 1
4 2
```

**Kimenet:**
```
1 3 1 2 4 2 5
```



### Algoritmus magyarázata

1. **Gráf reprezentáció:** A problémát egy irányított gráfként modellezhetjük, ahol a szintek a csúcsok, és a teleportálók az élek.

2. **Euler-út keresése:** A feladat lényegében egy Euler-út megtalálása az 1. csúcsból az n. csúcsba. Egy Euler-út olyan út, amely minden élt pontosan egyszer használ.

3. **Bemeneti és kimeneti fokok:** Ellenőrizni kell, hogy minden csúcs bemeneti foka megegyezik-e a kimeneti fokával, kivéve az 1. és n. csúcsot. Az 1. csúcsnak eggyel nagyobb kimeneti fokkal kell rendelkeznie, míg az n. csúcsnak eggyel nagyobb bemeneti fokkal.

4. **Hierholzer algoritmus:** Ha a fenti feltételek teljesülnek, használhatjuk a Hierholzer algoritmust az Euler-út megtalálására.

5. **Időbeli hatékonyság:** Az algoritmus időbonyolultsága O(m), ahol m a teleportálók (élek) száma.

6. **Megoldás ellenőrzése:** Végül ellenőrizni kell, hogy a talált út valóban az 1. szintről indul és az n. szinten végződik-e.


# Tesztelés

## Előfeltételek

- Python >= 3.8

- Virtuális környezet létrehozása:

```bash
python3 -m venv ./venv
```

- Virtuális környezet aktiválása

```bash
source ./venv/bin/activate
```

- Python csomagok telepítés

```bash
pip install -r requirements.txt
```


- Teszt fájlok megléte:
   - A különböző teszt különböző megoldások teszt fájljai a [tests](./tests/) mapáában taláhatóak előre feltöltve teszt példákkal 

## Towers of Hanoi

```bash
chmod +x run_test_hanoi.sh
bash run_test_hanoi.sh --test_path ./tests/hanoi/test.csv 
```

- ```Az algoritmus pontos lépései a ./logs/hanoi mappában található log fájlokban találhatóak```

## Sliding Window Median

```bash
chmod +x run_test_sliding_median.sh
bash run_test_sliding_median.sh --test_path tests/sliding_median/test.csv
```

## Counting Numbers

```bash
chmod +x run_test_counter.sh
bash run_test_counter.sh --test_path ./tests/counter/test.csv
```

## Teleporters Path

```bash
chmod +x run_test_teleporter.sh
bash run_test_teleporter.sh --test_path ./tests/teleporter/test.json
```