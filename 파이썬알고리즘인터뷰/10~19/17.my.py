# p17 : sort given linked-list according to its pair.

# next,next and swap

from LinkedList import ListNode

def paired_sort(head: ListNode) -> ListNode:
    front = head.next
    back = head

    while front.next:
        front.val, back.val = back.val, front.val
        front, back = front.next.next, back.next.next

    front.val, back.val = back.val, front.val

    return head

t1 = ListNode(val=1)
t2 = ListNode(val=2)
t3 = ListNode(val=3)
t4 = ListNode(val=4)

t1.next, t2.next, t3.next, t4.next = t2, t3, t4, None

result = paired_sort(t1)

while result:
    print(result.val)
    result = result.next

