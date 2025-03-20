class Node:
    def __init__(self,val = None, next = None):
        self.val = val
        self.next = next

def repair(p):
    head = Node(None,p)
    p = head
    even_numbers = Node()

    while p.next != None:
        if p.next.val % 2 == 0:
            tmp = p.next
            p.next = p.next.next
            tmp.next = even_numbers.next
            even_numbers.next = tmp
        else:
            p = p.next

    p.next = even_numbers.next
    return head.next

def list_to_linked_list(list):
    g = Node()
    for elem in list[::-1]:
        new_node = Node(elem, None)
        g.next = new_node
    return g

def print_list(head):
    while head != None:
        print(str(head.val) + " -> ", end="")
        head = head.next
        
    print("KONIEC")

l1 = list_to_linked_list([14,3,7,56,9,11])
l2 = repair(l1)
print_list(l2)
        