/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    
    private TreeNode Root;
    
    private boolean find(TreeNode p, int v){
        if(p==null)return false;
        if(v==p.val)return true;
        if(v<p.val)return find(p.left,v);
        return find(p.right,v);
    }
    
    public boolean findTargetHelper(TreeNode root, int k) {
        
        if(root==null)return false;
        //System.out.println(root.val+" "+k);
        if(k!=root.val*2 &&  find(Root,k-root.val))
            return true;
        return findTargetHelper(root.left,k)||findTargetHelper(root.right,k);
    }
    
    public boolean findTarget(TreeNode root, int k) {
        Root=root;
        //System.out.println(find(root,-2));
        return findTargetHelper(root,k);
        
    }
}
