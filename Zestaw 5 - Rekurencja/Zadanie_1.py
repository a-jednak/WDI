class node:
    def __init__(self, val):
        self.value = val
        self.next = None

def member(el, zb):
    while zb.value <= el:       #dla posortowanego zbioru
        if zb.value == el:
            return True
        zb = zb.next

    return False

def add(el, zb):
    pzb = None
    while zb != None and zb.value < el:
        pzb = zb
        zb = zb.next
    if zb != None and zb.value != el:
        pzb.next = node(el)
        pzb.next.next = zb
    elif zb == None and pzb != None:
        pzb.next = node(el)
        pzb.next.next = None
    else:                                 # zb i pzb są None
        zb = node(el)

def delete(el, zb):
    if zb != None:
        pzb = None
        while zb.value != el:
            pzb = zb
            zb = zb.next
        pzb.next = zb.next


x = 8
y = 10
z = 11
x1 = node(x)
x1.next = node(y)
node(y).next = node(z)

print(member(11, x1))