import collections
''' Data Stucture Tree for leetcode'''
class TreeNode:
    def __init__(self,value = None):
        self.value = value
        self.lchild= None
        self.rchild = None

    def print_value(self):
        print(self.value)

    def print_child(self):
        print(self.lchild)
        print(self.rchild)

class Tree:
    def __init__(self,root = None):
        self.root = root

    def add(self,node):
        if not self.root:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            if not cur.lchild:
                cur.lchild = node
                return
            elif not cur.rchild:
                cur.rchild = node
                return
            else:
                queue.append(cur.rchild)
                queue.append(cur.lchild)


tree_inorder_list = []
tree_preorder_list = []
tree_postorder_list = []
def inorder_travel(tree):
    if tree:
        inorder_travel(tree.lchild)
        tree_inorder_list.append(tree.value)
        inorder_travel(tree.rchild)
def preorder_travel(tree):
    if tree:
        tree_preorder_list.append(tree.value)
        preorder_travel(tree.lchild)
        preorder_travel(tree.rchild)
def postorder_travel(tree):
    if tree:
        postorder_travel(tree.lchild)
        postorder_travel(tree.rchild)
        tree_postorder_list.append(tree.value)


def get_all_travel_list(tree):
    preorder_travel(tree)
    inorder_travel(tree)
    postorder_travel(tree)
    print("preorder : ",tree_preorder_list)
    print("inorder : ",tree_inorder_list)
    print("postorder : ",tree_postorder_list)

def ret_lr_two_list(list,element):
    return list[:element],list[element:]

def level_order_display(root):
    '''
    dsiplay of the tree
    ! only after get_all_travel_list(tree)
    '''
    if not root:
        return
    temp = root
    que = [temp]
    tree_queue = []
    while len(que) > 0:
        # print(que[0].value, end=" ")
        temp = que.pop(0)
        tree_queue.append(temp.value)
        if temp.lchild:
            que.append(temp.lchild)
        if temp.rchild:
            que.append(temp.rchild)
    print(tree_queue)


def depth_of_tree(root):
    """
    Recursive function that returns the depth of a binary tree.
    """
    return 1 + max(depth_of_tree(root.lchild), depth_of_tree(root.rchild)) if root else 0


def main():  # Main function for testing.
    # tree = TreeNode(1)
    # tree.lchild = TreeNode(2)
    # tree.rchild = TreeNode(3)
    # tree.lchild.lchild = TreeNode(4)
    # tree.lchild.rchild = TreeNode(5)
    # tree.lchild.rchild.lchild = TreeNode(6)
    # tree.rchild.lchild = TreeNode(7)
    # tree.rchild.lchild.lchild = TreeNode(8)
    '''       1
         2         3
       4   5     7
          6    8
    '''

    root1 = TreeNode(3)
    root1.lchild = TreeNode(5)
    root1.rchild = TreeNode(1)
    root1.lchild.lchild=TreeNode(6)
    root1.lchild.rchild=TreeNode(2)
    root1.rchild.lchild=TreeNode(9)
    root1.rchild.rchild=TreeNode(8)
    root1.lchild.rchild.lchild=TreeNode(7)
    root1.lchild.rchild.rchild=TreeNode(4)
    #
    # root2 = TreeNode(3)
    # root2.lchild = TreeNode(5)
    # root2.rchild = TreeNode(1)
    # root2.lchild.lchild=TreeNode(6)
    # root2.lchild.rchild=TreeNode(7)
    # root2.rchild.lchild=TreeNode(4)
    # root2.lchild.rchild=TreeNode(2)
    # root2.rchild.rchild.lchild=TreeNode(9)
    # root2.rchild.rchild.rchild=TreeNode(8)




    get_all_travel_list(root1)
    print()
    level_order_display(root1)

if __name__ == "__main__":
    main()