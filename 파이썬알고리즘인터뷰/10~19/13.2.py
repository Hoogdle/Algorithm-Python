
# optimize by 'deque'

from LinkedList import ListNode
from collections import deque

def is_palindrome(head: ListNode) -> bool:

    l = deque()

    if head is None:
        return True

    node = head

    while node:
        l.append(node.val)
        node = node.next

    while len(l)>1:
        if deque.pop() != deque.popleft():
            return False

    return True


