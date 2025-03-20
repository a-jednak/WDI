# Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie określonej masy. Odważniki można umieszczać tylko na jednej szalce.

T = [12, 3, 4, 9, 10, 4, 4, 11, 7, 2]

def fun(T, x, waga=0, p=0):
    N = len(T)
    if waga == x:
        return True
    if p == N:
        return False
    return fun(T, x, waga+T[p], p+1) or fun(T, x, waga, p+1)

print(fun(T, 70))

