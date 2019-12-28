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
    bool isSymmetric(TreeNode* root) {
        if(root == nullptr) return true;
        return check_sym(root->left, root->right);
    }
    
private:
    bool check_sym(TreeNode* l, TreeNode* r){
        if(l == nullptr and r == nullptr) return true;
        else if(l == nullptr or r == nullptr) return false;
        return ((l->val == r->val) and check_sym( l->left, r->right) and check_sym(l->right, r->left)) ;
    }
};