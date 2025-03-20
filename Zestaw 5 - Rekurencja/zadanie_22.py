# Dana jest tablica T[N] zawierająca liczby naturalne. Po tablicy możemy przemieszczać się
# według następującej zasady: z pola o indeksie i możemy przeskoczyć na pole o indeksie i+k jeżeli k jest
# czynnikiem pierwszym liczby t[i] mniejszym od t[i]. Proszę napisać funkcję, która zwraca informację czy jest
# możliwe przejście z pola o indeksie 0 na pole o indeksie N-1. Funkcja powinna zwrócić liczbę wykonanych
# skoków lub wartość -1 jeżeli powyższe przejście nie jest możliwe.


T = [4,0,8,7,12,4,3,1] # N = 8

def zad22(T):
    res = -1
    N = len(T)

    def fun(i=0, cnt=0):
        nonlocal res
        if i == N-1:
           res = cnt
        a = T[i]
        k = 2
        while k<a:
          while a%k == 0:
              a //= k
              fun(i+k, cnt+1)
          k += 1

        res = max(res, -1)

    return res
  
print(zad22(T))
