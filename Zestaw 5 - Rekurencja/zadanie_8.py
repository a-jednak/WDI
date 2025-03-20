# Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie określonej masy. Odważniki można umieszczać tylko na jednej szalce.
# 8. ale odważniki można umieszczać na obu szalkach

T = [8, 2]

def fun(T, x, waga=0, p=0):
    N = len(T)
    if waga == x:
        return True
    if p == N:
        return False
    return fun(T, x, waga+T[p], p+1) or fun(T, x, waga, p+1) or fun(T, x+T[p], waga, p+1)

print(fun(T, 6))

