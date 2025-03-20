class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def find_first_ending_with_digit(p, digit):
    head = p
    cnt = 2
    while p.next != head:
        if str(p.next.val)[-1] == digit:
            return p.next, cnt                #zwracamy obiekt który spełnia warunek
        p = p.next
        cnt += 1
    return None, None

def insert(p, n):
    first_digit = str(n)[0]
    last_digit = str(n)[-1]
    g = Node(None, p)
    start = p
    p = g

    while True:
        if first_digit == str(p.next.val[0]):
            end, length = find_first_ending_with_digit(p.next, last_digit)
            if end == None:
                return 0
            new_node = Node(n, end.next)
            p.next = new_node
            return length
        else:
            p = p.next


        if p.next == start:
            break

