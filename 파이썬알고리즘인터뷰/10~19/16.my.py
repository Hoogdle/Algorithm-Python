# p16 : add given linked-list which has reversed order.

from LinkedList import ListNode

def two_sum(head1: ListNode, head2: ListNode) -> int:
    mul_num = 1
    result = 0

    while head1 or head2:
        if head1 and head2:
            result += (head1.val + head2.val) *  mul_num
            mul_num *= 10
            head1, head2 = head1.next, head2.next

        elif head1:
            result += (head1.val) * mul_num
            mul_num *= 10
            head1 = head1.next

        elif head2:
            result += (head2.val) * mul_num
            mul_num *= 10
            head2 = head2.next

    return result


a1 = ListNode(val=2)
a2 = ListNode(val=4)
a3 = ListNode(val=3)

b1 = ListNode(val=5)
b2 = ListNode(val=6)
b3 = ListNode(val=4)
b4 = ListNode(val=7)

a1.next, a2.next, a3.next = a2, a3, None
b1.next, b2.next, b3.next, b4.next = b2, b3, b4, None

print(two_sum(a1,b1))
