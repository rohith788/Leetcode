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
    bool isValidBST(TreeNode* root) {
        return check_bst(root, nullptr, nullptr);
    }
    
private:
    bool check_bst(TreeNode* root, TreeNode* max, TreeNode* min){
        if(root == nullptr) return true;
        if(max != nullptr and root->val >= max->val) return false;
        else if(min != nullptr and root->val <= min->val) return false;
        
        return check_bst(root->left, root, min) and check_bst(root->right, max, root);
    }
};