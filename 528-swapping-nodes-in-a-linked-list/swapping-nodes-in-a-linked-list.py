class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr=[]
        current=head
        c=0
        while current:
            arr.append(current.val)
            current=current.next
        current=head
        c=0
        while current:
            c+=1
            if c==k:
                current.val=arr[len(arr)-k]
            if c==len(arr)-k+1:
                current.val=arr[k-1]
            current=current.next
        return head