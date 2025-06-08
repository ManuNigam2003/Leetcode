class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        temp=head
        res=[]
        while temp:
            res.append(temp.val)
            temp=temp.next
        count=Counter(res)
        result=[]
        for key,value in count.items():
            if count[key]==1:
                result.append(key)      
        if not result:
            return None
        else:            
            new_node=ListNode(result[0])
            head=new_node
            prev=head
            for i in range(1,len(result)):
                new_node=ListNode(result[i])
                prev.next=new_node
                prev=new_node
                prev.next=None
            return head       


            
            