# p16 : add given linked-list which has reversed order.

from LinkedList import ListNode

def two_sum(head1: ListNode, head2: ListNode) -> ListNode:
    result_node = ListNode(val=0)
    return_node = result_node

    while head1 or head2:
        if head1 and head2:
            tmp = result_node.val + head1.val + head2.val
            if tmp >= 10:
                result_node.val = tmp%10
                result_node.next = ListNode(val=1)
            else:
                result_node.val = tmp
                result_node.next = ListNode(val=0)

            head1, head2 = head1.next, head2.next
            result_node = result_node.next

        elif head1:
            result_node.val = head1.val
            head1 = head1.next
            if head1:
                result_node.next = ListNode(val=0)
                result_node = result_node.next

        elif head2:
            result_node.val = head2.val
            head2 = head2.next
            if head2:
                result_node.next = ListNode(val=0)
                result_node = result_node.next

        result_node.next = None

    return return_node


a1 = ListNode(val=2)
a2 = ListNode(val=4)
a3 = ListNode(val=3)

b1 = ListNode(val=5)
b2 = ListNode(val=6)
b3 = ListNode(val=4)
b4 = ListNode(val=7)

a1.next, a2.next, a3.next = a2, a3, None
b1.next, b2.next, b3.next, b4.next = b2, b3, b4, None

result = two_sum(a1,b1)

while result:
    print(result.val)
    result = result.next
