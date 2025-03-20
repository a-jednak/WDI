# Zadanie 16.
# Proszę napisać funkcję, która otrzymując jako parametr
# wskazujący na początek listy jednokierunkowej, przenosi
# na początek listy te z nich, które mają parzystą ilość
# piątek w zapisie ósemkowym.

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

def osiem(x):
    y = 0
    pot = 0
    while x > 0:
        y += (x%8)*10**pot
        pot += 1
        x //= 8

    return y

def parz_5(y):
    cnt = 0
    while y>0:
        if y%10 == 5:
            cnt += 1
        y = y//10
    return True if cnt%2==0 else False

def przenosi(p):
    start = p
    halp = p
    halpp = Node()
    damn = halpp
    start.next = halp
    while p.next.val is not None:
        if parz_5(osiem(p.next.val)):
            r = p.next
            p = p.next.next
            r.next = None
            halp.next = r
            halp = halp.next 
            p = p.next
        else:
            halpp.next = p.next
            p = p.next
            halpp = halpp.next
    
    halp.next = damn.next

    return start


l = list_to_linked_list([5, 45, 2891, 331])
l = przenosi(l)
print_list(l)
        


