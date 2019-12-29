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
    ListNode* reverseList(ListNode* head) {
        ListNode* ans = NULL;
        ListNode* temp = head;
        while( temp != nullptr){
            ListNode* temp2 = temp->next;
            temp->next = ans;
            ans = temp;
            temp = temp2;
        }
        return ans;
    }
};
