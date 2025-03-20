# Zadanie 29.
# Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby 
# naturalne. W obu listach liczby są posortowane rosnąco.
# Proszę napisać funkcję usuwającą z każdej listy liczby nie występujące
# w drugiej. Do funkcji należy przekazać wskazania na obie listy,
# funkcja powinna zwrócić łączną liczbę usuniętych elementów.

class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def clear(p1,p2):

    cnt = 0
    while p1.next != None and p2.next != None:
        if p1.next.val < p2.next.val:
            p1.next = p1.next.next
            #p1 = p1.next
            cnt += 1
        elif p2.next.val < p1.next.val:
            p2.next = p2.next.next
            #p2 = p2.next
            cnt += 1
        else:
            p1 = p1.next
            p2 = p2.next

    while p1.next != None:
        cnt += 1
        p1 = p1.next

    while p2.next != None:
        cnt += 1
        p2 = p2.next

    return cnt

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


l1 = list_to_linked_list([3, 4, 9, 15, 21, 22, 30])
l2 = list_to_linked_list([2, 4, 17, 27])            
#print_list(l1)
x = clear(l1,l2)

print(x)



        