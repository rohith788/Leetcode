 /**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
      vector<vector<int>> arr;
      deque<TreeNode *> dq;
      dq.push_back(root);
      int lev = 0;
      while(!dq.empty()){
        ++lev;
        vector<int> blah;
        
        if(lev % 2 == 0){
          int n = dq.size();
          while(n --> 0){
            TreeNode *node = dq.back();
            dq.pop_back();
            if(node){
              blah.push_back(node->val);
              dq.push_front(node->right);
              dq.push_front(node->left);  
            }
          }
        }
        else{
          int n = dq.size();
          while(n --> 0){
            TreeNode *node = dq.front();
            dq.pop_front();
            if(node){
              blah.push_back(node->val);
              dq.push_back(node->left);
              dq.push_back(node->right); 
            }
          }
        }
        if(!blah.empty()) arr.push_back(std::move(blah));
      }
      return arr;
    }
};