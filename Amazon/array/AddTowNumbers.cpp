/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
      ListNode* head = NULL;  
      ListNode** temp = &head;
      int carry = 0;
      while(l1||l2){
        int val = carry;
        if(l1) val += l1->val;
        if(l2) val += l2->val;
        
        carry = val / 10;
        *temp = new ListNode ( val % 10);    
        temp = &((*temp)->next);
        
        if(l1) l1 = l1->next;
        if(l2) l2 = l2->next;        
      }
      if(carry) *temp = new ListNode(1);
      
      return head;
      
    }
};