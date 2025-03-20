# Zadanie 24.
# Dana jest lista, który zakończona jest cyklem.
# Napisać funkcję, która zwraca liczbę elementów przed cyklem.


class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def cycle(p):
    fast = p
    slow = p
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break

    cnt = 0
    slow2 = p
    while slow2 != fast:
        cnt +=1
        slow2 = slow2.next
        fast = fast.next

    return cnt