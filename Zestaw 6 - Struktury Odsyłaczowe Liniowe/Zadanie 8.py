# Zadanie 8.
# Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi
# element listy. Do funkcji należy przekazać wskazanie na pierwszy element listy.

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

def deletowanie(p):
    start = p
    while p.next != None: #and p.next.next != None:
        p.next = p.next.next
        if p.next != None:
            p = p.next
    return start


l = list_to_linked_list([0,1,2,3,4,5,6,7,8,9,10])
l = deletowanie(l)
print_list(l)