/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

#define NOT_BALANCED 100000

int checkBalanced(struct TreeNode* root, int deep) {
    if(root==NULL)return deep;
    int left=checkBalanced(root->left,deep+1);
    int right=checkBalanced(root->right,deep+1);
    if(left==NOT_BALANCED || right==NOT_BALANCED)
        return NOT_BALANCED;
    else if(left>=right && left-right<=1)
        return left;
    else if(right>left && right-left<=1)
        return right;
    else return NOT_BALANCED;
}

bool isBalanced(struct TreeNode* root) {
    return checkBalanced(root,0)!=NOT_BALANCED;
}
