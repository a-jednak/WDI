#  Proszę napisać funkcję, która jako parametr otrzymuje liczbę naturalną i zwraca 
#  sumę iloczynów elementów wszystkich niepustych podzbiorów zbioru podzielników pierwszych
#  tej liczby. Można założyć, że liczba podzielników pierwszych nie przekracza 20, zatem 
#  w pierwszym etapie funkcja powinna wpisać podzielniki do tablicy pomocniczej. 
#  Przykład: 60 → [2, 3, 5] → 2 + 3 + 5 + 2 ∗ 3 + 2 ∗ 5 + 3 ∗ 5 + 2 ∗ 3 ∗ 5 = 71

def czynniki(n):
    CZ = []
    a = 2
    while n>1:
        if n%a==0:
            CZ.append(a)
            while n%a==0:
                n //= a
        a+=1

    return CZ

def zad(x):
    suma = 0
    T = czynniki(x)

    def rek(iloczyn, i):
        nonlocal suma
        if(i == len(T)):
            suma += iloczyn
        else:
            rek(iloczyn*T[i], i+1)
            rek(iloczyn, i+1)

    rek(1,0)
    return suma-1

print(zad(60))