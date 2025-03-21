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

def print_list(p):
    while p.next != None:
        print(str(p.next.val) + " -> ", end="")
        p = p.next

    print("KONIEC")

def common_part(a,b):
    p = Node()
    start = p

    while a.next != None and b.next != None:
        if a.next.val < b.next.val:
            a = a.next
        elif b.next.val < a.next.val:
            b = b.next
        else:
            r = a.next
            a.next = a.next.next
            r.next = None
            p.next = r
            p = p.next
            b = b.next

    return start


l1 = list_to_linked_list([1,2,5,6,8,12,15])
l2 = list_to_linked_list([1,4,5,7,12,15,20])
l3 = list_to_linked_list([1,3,5,9,12,16,20])

res = common_part(l1,l2)
final = common_part(res, l3)
print_list(final)