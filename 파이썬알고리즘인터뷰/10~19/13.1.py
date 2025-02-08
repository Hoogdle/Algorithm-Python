# p13 : check whether given list is palindrome

# make as list and check palindrome

# *** assume linked-list is given by name 'head' and member name of value is 'val'

from LinkedList import ListNode

def is_palindrome(head: ListNode) -> bool:
    l = []

    if not head:
        return True

    node = head

    while node is not None:
        l.append(node.val)
        node = node.next

    while len(l) > 1:
        if l.pop != l.pop(0):
            return False

    return True

