

# using iterative method
# using python multiple assignment(note that sequence of left side is important)
# left-hand : dynamic
# right-hand : static

from LinkedList import ListNode

def reverse_list(head: ListNode) -> ListNode:

    node,prev = head, None

    while node:
        prev, node.next, node = node, prev, node.next

    return prev

e1 = ListNode(val=1)
e2 = ListNode(val=2)
e3 = ListNode(val=3)
e4 = ListNode(val=4)
e5 = ListNode(val=5)

e1.next, e2.next, e3.next, e4.next, e5.next = e2, e3, e4, e5, None

reversed_list = reverse_list(e1)

while reversed_list:
    print(reversed_list.val)
    reversed_list = reversed_list.next