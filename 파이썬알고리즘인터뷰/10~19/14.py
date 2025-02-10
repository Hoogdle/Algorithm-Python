# connect given two-linked-list

# one-result-list, two-comparing-list

from LinkedList import ListNode
def connect_linked_list(former: ListNode, latter: ListNode) -> ListNode:
    start_position = None

    if former.val < latter.val:
        start_position = former
        former = former.next
    else:
        start_position = latter
        latter = latter.next

    linker = start_position
    while linker:
        if not former and not latter:
            linker.next = None
            break

        elif former and latter:
            if former.val < latter.val:
                linker.next = former
                linker = linker.next
                former = former.next
            else:
                linker.next = latter
                linker = linker.next
                latter = latter.next

        elif former or latter:
            if former and not latter:
                linker.next = former
                linker = linker.next
                former = former.next

            if latter and not former:
                linker.next = latter
                linker = linker.next
                latter = latter.next

    return start_position


a1 = ListNode(val=1)
a2 = ListNode(val=2)
a3 = ListNode(val=4)

a1.next = a2
a2.next = a3
a3.next = None

b1 = ListNode(val=1)
b2 = ListNode(val=3)
b3 = ListNode(val=4)

b1.next = b2
b2.next = b3
b3.next = None

result = connect_linked_list(a1,b1)

while result is not None:
    print(result.val)
    result = result.next