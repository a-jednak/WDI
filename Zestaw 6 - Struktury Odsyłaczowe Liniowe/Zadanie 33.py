# Zadanie 33.
# Napis s1 poprzedza napis s2 jeżeli ostatnia litera s1 jest „mniejsza” od pierwszej litery s2.
# Według tej zasady rozmieszczono napisy w liście cyklicznej, na przykład:
# -> bartek -> leszek -> marek -> ola -> zosia -------
# Proszę napisać stosowne definicje typów oraz funkcję wstawiającą do listy napis z zachowaniem
# zasady poprzedzania. Do funkcji należy przekazać wskaźnik do listy oraz wstawiany napis,
# funkcja powinna zwrócić wartość logiczną wskazującą, czy udało się wstawić napis do listy.
# Po wstawieniu elementu wskaźnik do listy powinien wskazywać na nowo wstawiony element.

class Node:
    def __init__(self, s = None, next = None):
        self.s = s
        self.next = next


def insert(p, napis):
    cycle = p
    tail = p
    p = p.next
    first_letter = napis[0]
    last_letter = napis[-1]
    while p.next != cycle:
        if ord(tail.next.s[-1]) < ord(first_letter) and ord(last_letter) < ord(p.next.s[0]):
            p = tail.next.next
            return True
        tail = p
        p = p.next
    
    return False


a = Node("bartek")
b = Node("leszek")
c = Node("marek")
d = Node("ola")
e = Node("zosia", a)

a.next = b
b.next = c
c.next = d
d.next = e

print(insert(a, "cool"))