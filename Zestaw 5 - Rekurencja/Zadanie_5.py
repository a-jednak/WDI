# Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
# na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
# każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
# 110100 nie jest możliwe.


def is_prime(x):
    if x < 2:
        return False
    if x==2 or x==3 or x==5:
        return True
    if not x%2 or not x%3 or not x%5:
        return False

    i = 7
    while i*i < x:
        if not x%i:
            return False
        i += 4
        if not x%i:
            return False
        i += 2

    return True

def decimal(T):
    res = 0
    N = len(T)
    for i in range(N):
        res += (2**(N-i-1))* T[i]
    return res

def uhhh(T):
    
    def zad5(T, p, k):
        N = len(T)
        if k > N-1:
            return False

        if k == N-1:
            if T[k] == 0 and k-p+1 != 2:
                return False
            return is_prime(decimal(T[p:k+1]))

        if is_prime(decimal(T[p:k+1])):
            return zad5(T, k+1, k+2)

        return zad5(T, p, k+1)

    return zad5(T, 0, 1) if len(T)>1 else False

T = [1,0,1]

print(uhhh(T))

