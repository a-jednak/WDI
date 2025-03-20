# Na szachownicy o wymiarach N × N umieszczono pewną liczbę pionków.
# Położenie pionków opisuje lista [(w0, k0),(w1, k1),(w2, k2), ...]. W lewym górnym rogu 
# szachownicy (o współrzędnych 0, 0) znajduje się król, który musi dotrzeć do prawego 
# dolnego rogu szachownicy. Król może wykonywać ruchy w prawo, w dół lub w górę 
# szachownicy, nie może zbijać pionków ani wracać na pole, na którym już był. 
# Proszę napisać funkcję king(N,L), która zwróci maksymalną liczbę ruchów jakie 
# może wykonać król na drodze do celu. Do funkcji należy przekazać wyłącznie dwa parametry:
# rozmiar szachownicy N oraz listę L zawierającą położenia pionków. 
# Jeżeli dotarcie do celu nie jest możliwe funkcja powinna zwrócić wartość None.

# Ruchy Króla: prawo, dół, góra
# Nie może wracać na pole na którym już był
# Cel: w,k == N-1
# res - maksymalna liczba ruchów króla


def king(N, L):

    def rek(w,k,cnt,T):
        T.append((w,k))
        maxi = 0
        if w == k == N-1:
            return cnt
        if w>=N or k>=N or w<0:
            return 0
        if (w+1,k) not in L and (w+1,k) not in T:
            maxi = max(maxi, rek(w+1,k,cnt+1,T))
        if (w,k+1) not in L and (w,k+1) not in T:
            maxi = max(maxi, rek(w,k+1,cnt+1,T))
        if (w-1,k) not in L and (w-1,k) not in T:
            maxi = max(maxi, rek(w-1,k,cnt+1,T))

        return maxi

    if rek(0,0,0,[]) > 0:
        return rek(0,0,0,[])
    return None


print(king(4,[(2,0),(2,1),(2,2),(2,3)]))

