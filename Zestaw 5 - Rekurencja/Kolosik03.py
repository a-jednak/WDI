# Na szachownicy o rozmiarach N × N reprezentowanej przez tablicę T[N][N] umieszczono pewną liczbę
# wież szachowych tak, że każde z wolnych pól na szachownicy jest szachowane. Położenie wież w tablicy
# oznaczono wartościami True. Przyszedł zły człowiek i zmienił położenie jednej z wież na szachownicy, tak że
# nie wszystkie wolne pola są szachowane. Proszę zaproponować funkcję move(T), która znajdzie przeniesienie
# jednej wieży, tak aby ponownie wszystkie pola były szachowane. Do funkcji przekazujemy tablicę T zawierającą 
# położenie wież po zmianie położenia wieży. Funkcja powinna zwrócić dwa pola (wiersz, kolumna) –
# skąd i dokąd należy przenieść wieżę.


def move(T):
    N = len(T)
    
    for i in range(N):
        check1 = 1
        
        for j in range(N):
            if T[i][j]:
                check1 = 0
                break
        if check1:
            a = i
            break

    for j in range(N):
        check1 = 1
        for i in range(N):
            if T[i][j]:
                check1 = 0
                break
        if check1:
            b = j
            break
    szach = (a, b) # dokąd przenieść wieżę

    print(szach)



#move([[True,True,False,True],[False,False,False,True],[False,False,False,False],[False,True,False,False]])