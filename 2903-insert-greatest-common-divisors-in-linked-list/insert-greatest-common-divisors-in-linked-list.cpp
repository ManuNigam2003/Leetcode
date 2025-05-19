class Solution {
public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
         ListNode *root=head;
         while(root->next){
             if(root->next){
                 int val=__gcd(root->val,root->next->val);
                 ListNode *tem=new ListNode(val);
                 tem->next=root->next;
                 root->next=tem;
                 
             }
             root=root->next->next;
         }
         return head;
    }
};