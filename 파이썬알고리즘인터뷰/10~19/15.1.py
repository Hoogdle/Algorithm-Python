

# using Recursive method.
# using python multiple-assignment => using 'two-pointer'

from LinkedList import ListNode

def reverse_list(head: ListNode) -> ListNode:
    def reverse(prev, node):
        if not node:
            return prev

        node.next, next = prev, node.next
        return reverse(node,next)

    return reverse(None, head)