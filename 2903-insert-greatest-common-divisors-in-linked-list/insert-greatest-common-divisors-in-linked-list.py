import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next==None:
            return head
        current=head
        while current and current.next:
            x=math.gcd(current.val,current.next.val)
            new_node=ListNode(x)
            new_node.next=current.next
            current.next=new_node
            current=current.next.next
        return head
        