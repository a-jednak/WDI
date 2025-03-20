

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
    

def print_list(head):
    while head != None:
        print(str(head.val) + " -> ", end="")
        head = head.next
        
    print("KONIEC")

def print_wartownik(head):
    print("GUARDIAN -> ", end ="")
    while head.next != None:
        print (str(head.next.val) + " -> ", end="")
        head = head.next

    print("KONIEC")

def remove_el(p, to_del):
    prev = None
    start = p
    while p != None:
        if p.val == to_del:
            if prev == None:    #usuwamy pierwszy element listy
                return p.next
            else:
                prev.next = prev.next.next
                return start

        prev = p
        p = p.next

    return start

def remove_watownik(p, to_del):
    start = p
    while p.next != None:
        if p.next.val == to_del:
            p.next = p.next.next
            return start

        p = p.next

    return start


def add_el(p, to_add):  #dodawnie na koniec listy
    start = p
    prev = None
    while p != None:
        prev = p
        p = p.next

    if prev == None:
        return Node(to_add)
    else:
        prev.next = Node(to_add)
    return start

def add_wartownik(p, to_add):
    start = p
    while p.next != None:
        p = p.next
    
    p.next = Node(to_add)
    return start


c = Node(3)
b = Node(2,c)
a = Node(1,b)
g = Node(None, a) #wartownik

print_list(a)
#a = remove_el(a,1)
#print_list(a)
a = add_wartownik(g,5)
print_wartownik(g)