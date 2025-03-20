# Zadanie 2. 
# Zastosowanie listy odsyłaczowej do implementacji tablicy rzadkiej. 
# Proszę napisać trzy funkcje:
# – inicjalizującą tablicę, 
# – zwracającą wartość elementu o indeksie n,
# – podstawiającą wartość value pod indeks n.

# tablica rzadka - tablica która w większości zawiera 0/Nulle

class Node:
    def __init__(self, val=None, index = None, next=None):
        self.val = val
        self.index = index
        self.next = next

def init():         # inicjalizacja listy
    return Node()

def get(p, index):
    while p.next != None:
        if p.next.index == index:
            return p.next.val
        elif p.next.index > index:
            return 0
        p = p.next

def add(p, index, value):
    start = p
    while p.next != None and p.next.index < index:  # gdy wyjdziemy z pętli mamy 2 przypadki -> albo indeks już istnieje albo nie
        p = p.next

    if p.next != None and p.next.index == index:
        p.next.val = value
    else:
        new_node = Node(value, index, p.next)
        p.next = new_node

    return start


g = init()      #inicjalizacja wartownika
