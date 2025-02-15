# p19: reverse the order of linked-list from m to n.

from LinkedList import ListNode

def reverse_m2n(head: ListNode, m: int, n:int) -> ListNode:
    saved_m = None
    saved_prev_m = None

    tail, node = None, head

    for i in range(m-1):
        tail, node = node, node.next

    # node point m's node
    # tail point (m-1)'s node
    saved_prev_m, saved_m = tail, node

    tail, node = node, node.next
    for i in range(n-m):
        lead = node.next
        tail, node.next, node = node, tail, lead

    # tail point n's node
    # node point (n+1)'s node

    saved_prev_m.next = tail
    saved_m.next = node

    return head

t1 = ListNode(val=1)
t2 = ListNode(val=2)
t3 = ListNode(val=3)
t4 = ListNode(val=4)
t5 = ListNode(val=5)

t1.next, t2.next, t3.next, t4.next, t5.next, = t2, t3, t4, t5, None

result = reverse_m2n(t1, 2 ,4)

while result:
    print(result.val)
    result = result.next

