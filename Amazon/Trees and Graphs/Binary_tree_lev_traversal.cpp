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
    vector<vector<int>> arr;
    vector<vector<int>> levelOrder(TreeNode* root) {
        array_mode(root, 0);
        return arr;
    }
private:
    void array_mode(TreeNode* node,int lev){
        if(node == nullptr) return; 
        if(arr.size() == lev) arr.push_back(vector<int>());
        arr[lev].push_back(node->val);
        if(node->left != nullptr) array_mode(node->left, lev+1);
        if(node->right != nullptr) array_mode(node->right, lev+1);
    }
        
};