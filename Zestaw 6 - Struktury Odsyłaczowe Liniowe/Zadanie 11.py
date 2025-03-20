# Zadanie 11.
# Lista zawiera niepowtarzające się elementy.
# Proszę napisać funkcję do której przekazujemy
# wskaźnik na początek oraz wartość klucza. Jeżeli element
# o takim kluczu występuje w liście należy go usunąć z listy.
# Jeżeli elementu o zadanym kluczu brak w liście należy element
# o takim kluczu wstawić do listy.


class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def list_to_linked_list(list):
    g = Node()
    for elem in list[::-1]:
        new_node = Node(elem, g.next)
        g.next = new_node
    return g

def print_list(head):
    while head is not None:
        print(str(head.val) + " -> ", end = "")
        head = head.next
    print("KONIEC")

def is_member(p,k):
    while p.next != None:
        if p.next.val == k:
            return True
        p = p.next
    
    return False


def funkcja(p, k):
    start = p
    if not is_member(p, k):         
        tmp = p.next
        p.next = Node(k, tmp)
        return start
    else:                           
        tmp = p
        while p.next != None:
            if p.next.val == k:
                break
            tmp = p
            p = p.next
        
        tmp.next = p.next.next

    return start  



l = list_to_linked_list([2,4,6,12,66,31,3])
l = funkcja(l, 3)
print_list(l)
