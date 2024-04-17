class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        # node-object, with a value and the possibility for a left and right branch
        self.val = value
        self.left = left
        self.right = right
        
def create_tree(numbers: list) -> TreeNode:
    #TODO create the tree from the list of numbers
    # objects are easier to handle
    
    if not numbers:
        return None
    # trying to explain... a def inside a def is a nested function used for recursive calls
    # so 'add_root' is called over and over again till the end of the list
    def add_root(i):
        if i < len(numbers):
            # remember the example [4,8,5,0,1,None,6]
            # first iteration i is 0, so root is 4, root.left is 8 and right is 5
            # 2nd i is 1, so root is 8, left is 0, right is 1 and so on...
            root = TreeNode(numbers[i])
            root.left = add_root(2 * i +1)
            root.right = add_root(2 * i +2)
            
            return root
        return None
    
    tree =  add_root(0)
    print_tree(tree)
    return tree

def average_root(numbers: list) -> int:
    
    # TODO: Count Nodes Equal to Average of Subtree
    tree = create_tree(numbers)
    
    root_count = 0
    tree_vals = []
    
    def get_sum_and_count(node):
        if not node:
            return 0, 0, 0  # subtree sum, subtree count, nodevalue
        
        left_subtree_sum, left_subtree_count, _ = get_sum_and_count(node.left)
        right_subtree_sum, right_subtree_count, _ = get_sum_and_count(node.right)
        
        subtree_sum = left_subtree_sum + right_subtree_sum + node.val if node.val is not None else 0
        subtree_count = left_subtree_count + right_subtree_count + 1 if node.val is not None else 0
        
        tree_vals.append((subtree_sum, subtree_count, node.val))

        return subtree_sum, subtree_count, node.val
    
    get_sum_and_count(tree)
    
    for subtree_sum, subtree_count, subtree_val in tree_vals:
        average = (subtree_sum // subtree_count) if subtree_count>0 else 0
        #print(subtree_sum, subtree_count, subtree_val, average == subtree_val)
        if average == subtree_val:  # Check if root value equals the average
            root_count += 1
            
    return root_count

### just for visualisation
def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print("   " * level + str(node.val))
        print_tree(node.left, level + 1)

if __name__ == "__main__":
    
    #      4
    #     / \
    #    8   5
    #   / \    \
    #  0   1    6

    # Node 4: The subtree sum is 24 (4 + 8 + 0 + 1 + 5 + 6), 
    # and the count is 6. The average is 24 // 6 = 4. 
    # The value of node 4 is equal to the average of its subtree. 
    # So, we count this node.

    # Node 8: The subtree sum is 9 (8 + 0 + 1), 
    # and the count is 3. The average is 9 // 3 = 3. 
    # The value of node 8 is not equal to the average of its subtree. 
    # So, we don't count this node.

    # Node 5: The subtree sum is 11 (5 + 6), and the count is 2. 
    # The average is 11 // 2 = 5. 
    # The value of node 5 is equal to the average of its subtree. 
    # So, we count this node.

    # Node 0: The subtree sum is 0, and the count is 1. 
    # The average is 0 // 1 = 0. 
    # The value of node 0 is equal to the average of its subtree. 
    # So, we count this node.

    # Node 1: The subtree sum is 1, and the count is 1. 
    # The average is 1 // 1 = 1. 
    # The value of node 1 is equal to the average of its subtree. 
    # So, we count this node.

    # Node 6: The subtree sum is 6, and the count is 1. 
    # The average is 6 // 1 = 6. 
    # The value of node 6 is equal to the average of its subtree. 
    # So, we count this node.
    
    print("Example 1: ", average_root([4,8,5,0,1,None,6])) # 5
    print('*'*20)
    print("Example 2: ", average_root([1])) # 1
    