# W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla
# nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na
# polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu
# (np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica
# T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne
# w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego
# narożnika.

# prawy dolny narożnik -> w=7 k=7 (N-1)
# ruch nie może oddalać -> ani w górę ani w lewo
# ruch możliwy -> ostatnia cyfra liczby na polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego

def cyfry(x):
    a = x%10   # cyfra ostatnia
    b = x//10**(len(str(x))-1)  # cyfra pierwsza
    return (b, a)

def walk(a, b):     # a - pole na ktorym stoi, b - pole gdzie chce przejść
    return cyfry(a)[1] < cyfry(b)[0]

def zad(T):
    N = 4
    
    def rek(w, k):
        if w == k == N-1:
            return True
        if w < N-1 and k < N-1:
            if walk(T[w][k], T[w+1][k]):
                return rek(w+1,k)
            if walk(T[w][k], T[w+1][k+1]):
                return rek(w+1,k+1)
            if walk(T[w][k], T[w][k+1]):
                return rek(w, k+1)

        if w==N-1:
            if walk(T[w][k], T[w][k+1]):
                return rek(w, k+1)
            else:
                return False

        if k==N-1:
            if walk(T[w][k], T[w+1][k]):
                return rek(w+1, k)
            else:
                return False

    return rek(0,0)

        

T = [[12,36,78,91],[1,72,1,1],[1,34,51,55],[1,1,32,61]]

print(zad(T))