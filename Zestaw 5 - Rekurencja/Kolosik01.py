# Na szachownicy o wymiarach Nx N umieszczono pewną liczbę pionków. Położenie pionków opisuje lista [(w0, k0), (w₁, k₁), (w₂,k₂),...].
# W lewym górnym rogu szachownicy (o współrzędnych 0,0) znajduje się wieża, która musi dotrzeć do prawego dolnego rogu szachownicy.
# Wieża może wykonywać ruchy w prawo lub w dół szachownicy i nie może zbijać pionków. Proszę napisać funkcję rook (N,L), która zwróci
# minimalną liczbę ruchów jakie musi wykonać wieża aby dotrzeć do celu. Do funkcji należy przekazać wyłącznie dwa parametry:
# rozmiar szachownicy N oraz listę L zawierającą położenia pionków. Jeżeli dotarcie do celu nie jest możliwe funkcja powinna
# zwrócić wartość None.

def rook(N,L):
   
    def rek(w,k,cnt):
        mini = float('inf')
        if w == N-1 and k == N-1:
            return cnt

        if w >= N or k >= N:
            return float('inf')

        for i in range(w+1, N):
            if (i, k) in L:
                break
            mini = min(mini, rek(i, k, cnt+1))

        for j in range(k+1, N):
            if (w, j) in L:
                break
            mini = min(mini, rek(w,j,cnt+1))

        return mini

    return rek(0,0,0)



N = 3
L = [(0,1), (1,2)]

print(rook(N,L))
