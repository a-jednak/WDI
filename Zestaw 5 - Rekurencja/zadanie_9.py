# Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie określonej masy. Odważniki można umieszczać tylko na jednej szalce.
# 9. Program powinien wypisywać wybrane odważniki

T = [8, 2, 10, 7, 3]

def fun(T, x, waga=0, p=0, s=""):
    N = len(T)
    if waga == x:
        return s
    if p == N:
        return
    return fun(T, x, waga+T[p], p+1, s+str(T[p])+" ") or fun(T, x, waga, p+1, s)

print(fun(T, 30))

