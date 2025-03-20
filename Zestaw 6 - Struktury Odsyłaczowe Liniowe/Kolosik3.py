# Zadanie 5 (5 pkt)
# Dwie liczby naturalne są czynnikowo-podobne, jeżeli w swoich rozkładach na czynniki pierwsze mają
# okładnie jeden czynnik równy. Na przykład: 24 i 14 albo 32 i 18. Dana jest tablica T[N][N]
# zawierająca liczby naturalne. Dwie liczby sąsiadują ze sobą wtedy, gdy leżą w sąsiednich kolumach i
# sąsiednich wiersza. Proszę napisać funkcję three(T), która zwraca ilość liczb w tablicy sąsiadujących
# dokładnie z 3 liczbami czynnikowo-podobnymi.

def czynnikowo_podobne(x,y):
    a = 2
    flag = 0
    while x>1 and y>1:
        if x%a == 0 and y%a == 0:
            flag += 1
        while x%a == 0:
            x = x//a
        while y%a == 0:
            y = y//a
        a += 1

    if flag==1:
        return True 
    return False

#print(czynnikowo_podobne(32,18))

def zad(T):
    N = len(T)
    res = 0
    for i in range(1, N):
        for j in range(1, N):       #nie ma co sprawdzać krawędzi tablicy bo tam mają maksymalnie 2 sąsiadów
            a = T[i][j]
            cnt = 0
            for w in range(i-1,i+2):
                for k in range(j-1,j+2):
                    if w != i and k != j: #mogą być sąsiadami
                        if czynnikowo_podobne(a, T[w][k]):
                            cnt += 1
            if cnt == 3:
                res += 1

    return res


