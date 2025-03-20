

def deleteK(p, k):
    start = p
    cnt = 0

    while True:
        cnt += 1
        p = p.next
        if p == start:
            break

    T = [0] * cnt
    cnt = 0

    while True:
        T[cnt] = p.val
        cnt += 1
        p = p.next
        if p == start:
            break

    while p.next != start:
        if T.count(p.next.val) == k:
            p.next = p.next.next
        else:
            p = p.next