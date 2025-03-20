# Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, która odpowiada
# na pytanie, czy spośród (niekoniecznie wszystkich) elementów tablicy można utworzyć dwa podzbiory o
# jednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k. Do funkcji należy przekazać
# wyłącznie tablicę T oraz liczbę naturalną k, funkcja powinna zwrócić wartość typu bool.

# SUMA MOCY obu podzbiorów wynosiła k.


def zad(T, k):      #zwraca wynik

    def rek(i, s1=0, s2=0, cnt1=0, cnt2=0):
        if i == len(T):
            return s1 == s2 and cnt1+cnt2 == k

        if cnt1 + cnt2 < k:
            return rek(i+1, s1+T[i], s2, cnt1+1, cnt2) or rek(i+1, s1, s2+T[i], cnt1, cnt2+1) or rek(i+1, s1, s2, cnt1, cnt2)
        else:
            rek(i+1, s1, s2, cnt1, cnt2)

    return(rek(0))


print(zad([16,3,1,1,1,1,1], 3))