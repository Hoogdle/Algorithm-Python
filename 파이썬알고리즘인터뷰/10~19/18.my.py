# p18 : Sort Linked-List in order which put sequence of odd firstly, then even, with O(1) (Space), O(n) (Time)

# Odd-then-Even-Linking
# same with solution of book!

from LinkedList import ListNode

def odd_even_list(head: ListNode) -> ListNode:
    odd = head
    even = head.next
    head_even = head.next

    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    odd.next = head_even

    return head

t1 = ListNode(val=2)
t2 = ListNode(val=1)
t3 = ListNode(val=3)
t4 = ListNode(val=5)
t5 = ListNode(val=6)
t6 = ListNode(val=4)
t7 = ListNode(val=7)

t1.next, t2.next, t3.next, t4.next, t5.next, t6.next, t7.next = t2, t3, t4, t5, t6, t7, None

result = odd_even_list(t1)

while result:
    print(result.val)
    result = result.next
