

# using recursive-method

from LinkedList import ListNode

def swap_pairs(head: ListNode) -> ListNode:
    result = head.next

    def swap(back: ListNode, front: ListNode):
        next = front.next

        # for dealing error, occurred at last time
        if next is None:
            front.next, back.next = back, None
            return None

        front.next, back.next = back, next.next
        return swap(next, next.next)

    swap(head, head.next)
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

