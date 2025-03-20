# Zadanie 25.
# Dana jest lista, który zakończona jest cyklem.
# Napisać funkcję, która zwraca wskaźnik do
# ostatniego elementu przed cyklem.

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

def cycle(p):
    fast = p
    slow = p
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    slow = p
    while slow != fast:
        tail = slow
        slow = slow.next
        fast = fast.next

    return tail


a = Node(13)
b = Node(2)
c = Node(8)
d = Node(4)
e = Node(15)
f = Node(10)
g = Node(1, e)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

x = cycle(a)
print(x.val)
