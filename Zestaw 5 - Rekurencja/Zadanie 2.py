#Zestaw 5 Zad 2
# ”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
# waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
# naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
# równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.

T = [2, 2, 2, 2, 2, 2]

def waga(x):
    T = [0 for _ in range(100)]
    if x == 1:
        return 0
    a = 2
    while x > 1:
        while x%a == 0:
            T[a] += 1
            x = x//a
        a += 1

    l = 0
    for i in range(100):
        if T[i] > 0:
            l += 1

    return l

def zad(T):
    N = len(T)
    W = [waga(T[i]) for i in range(N)]

    def zad_rek(W, i=0, s1=0, s2=0, s3=0):
        N = len(W)
        if i == N:
            return (s1 == s2 == s3)
        return zad_rek(W, i+1, s1+W[i], s2, s3) or zad_rek(W, i+1, s1, s2+W[i], s3) or zad_rek(W, i+1, s1, s2, s3+W[i])

    return zad_rek(T)
            

print(zad(T))