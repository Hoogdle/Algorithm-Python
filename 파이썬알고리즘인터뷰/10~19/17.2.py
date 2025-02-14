
# change linked-list's link(not value) with iterative way.
# pair-wise-link-change

from LinkedList import ListNode

def swap_pairs(head: ListNode) -> ListNode :
    # prev, back, front, next

    # for excepting error, which occurred at first time
    result = head.next
    back, front, next = head, head.next, head.next.next
    front.next, back.next = back, next.next

    while next:
        front = next.next
        back = next
        next = front.next # if next nulled, break

        front.next, back.next = back, next

    return result

t1 = ListNode(val=1)
t2 = ListNode(val=2)
t3 = ListNode(val=3)
t4 = ListNode(val=4)

t1.next, t2.next, t3.next, t4.next = t2, t3, t4, None

result = swap_pairs(t1)

while result:
    print(result.val)
    result = result.next
