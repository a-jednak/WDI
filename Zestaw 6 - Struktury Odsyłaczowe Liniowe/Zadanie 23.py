# Zadanie 23.
# Dana jest lista, który zakończona jest cyklem.
# Napisać funkcję, która zwraca liczbę elementów w cyklu.

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

    cnt = 1
    slow = slow.next
    while slow != fast:
        cnt += 1
        slow = slow.next

    return cnt