class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if(!head || !head->next)return head;
        ListNode* prev= head;
        ListNode* curr= prev->next;
        ListNode* join = curr;
        while(curr && curr->next){
            prev->next = curr->next;
            prev = prev->next;

            curr->next = prev->next;
            curr = curr->next;


        }
        prev->next= join;
        return head;
        
    }
};