
# Defining a binary tree node
# Making a node with x as its value and initializing it's left and right child as null (None in python)
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


# Define a function that takes 2 inputs basically 2 nodes
# Making own function to test the similarity. Make sure to declare before you can use the function. Otherwise
# you get an error 'not declared' .We are using recursive calls here as the problem resembles recursive technique.

def isSametree(s, t):
    if s==None or t==None:
        return s==None and t==None
    elif s.val == t.val:
        return isSametree(s.left,t.left) and isSametree(s.right,t.right)
    else:
        return False


def isSubtree(s: TreeNode, t: TreeNode):
        # If the tree 's' is null, there is no point of considering tree 't' as it subtree, so return false
    if s==None:
        return False
    if isSametree(s,t):
        return True
    else:
        return isSubtree(s.left,t) or isSubtree(s.right,t)



# Lets write a testing code

S = TreeNode(3)
S.left = TreeNode(4)
S.right = TreeNode(5)
S.left.left = TreeNode(1)
S.left.right = TreeNode(2)

T = TreeNode(3)
T.left = TreeNode(4)
T.right = TreeNode(5)

print(isSubtree(S,T))

S1 = TreeNode(3)
S1.left = TreeNode(4)
S1.right = TreeNode(5)
S1.left.left = TreeNode(1)
S1.left.right = TreeNode(2)

T1 = TreeNode(4)
T1.left = TreeNode(1)
T1.right = TreeNode(2)

print(isSubtree(S1,T1))

'''Method Used = Recursion, 
Time complexity = O(MN)..... M = nodes in S and N = nodes in T
'''