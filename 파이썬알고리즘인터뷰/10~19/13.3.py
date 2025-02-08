

# using 'runner-method'

# fast-runner : alert to end point
# slow-runner : be in middle of list when fast-runner arrived end

# not None => True
# None => False

from LinkedList import ListNode

def is_palindrome(head: ListNode) -> bool:

    slow,fast = head
    prev = None

    while fast and fast.next:
        fast = fast.next.next

        # change order of half list(reverse)
        prev, prev.next, slow = slow, prev, slow.next

    if fast:
        slow = slow.next

    while slow and slow.val == prev.val:
        slow, prev = slow.next, prev.next

    return not slow


