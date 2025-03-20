# Zadanie 26.
# Proszę napisać funkcję, która sprawdza czy jedna lista zawiera się w drugiej. Do funkcji należy
# przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wartość logiczną.


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



def zawiera(p1, p2):
    x = p1
    while x.next != None:
        y = p2
        while y.next != None:
            if y.next.val == x.next.val:
                break
            y = y.next
        else:
            break
        
        x = x.next
    else:
        return True

    y=p2
    while y.next != None:
        x = p1
        while x.next != None:
            if x.next.val == y.next.val:
                break
            x = x.next
        else:
            break
        
        y = y.next
    else:
        return True

    return False

    


l1 = list_to_linked_list([1,2,3,5,6])
l2 = list_to_linked_list([1,2,3,4,5,6,7,8,9])

print(zawiera(l1,l2))