from tree import node
from tree import inorder
from tree import preorder
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum=0
        x=add_to(root,sum)
        print(x)
list_no=[]
def final_fn(root,count):
    if root:
        
        if root.right:
           x= add_to(root.right,count+root.right.val)
           list_no.append(x+root.val)
           final_fn(root.right,count)
        
        if root.left:
            y=add_to(root.left,count+root.left.val)
            
            list_no.append(y+root.val)
            final_fn(root.left,count)




def add_to(root,sum_no):
    if root:
        
        if root.right:
            return add_to(root.right,sum_no+root.right.val)
        
        if root.left:
            return add_to(root.left,sum_no+root.left.val)
    return sum_no
                
            

        
n=node(1)
n.insert(2)
n.insert(3)

# n.insert(15)
# n.insert(7)
# inorder(n,[])
# s=Solution()
# s.maxPathSum(n)
print(final_fn(n,0))
print(list_no)
# if __name__=="__main__":
#     type_hint(12)