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

def postorder_travel(tree,tree_postorder_list):
    if tree:
        postorder_travel(tree.lchild,tree_postorder_list)
        postorder_travel(tree.rchild,tree_postorder_list)
        if tree.lchild == None and tree.rchild == None:
            tree_postorder_list.append(tree.value)
    return tree_postorder_list

def dfs(root,result):
    if root is None:
        return
    if root.lchild is None and root.rchild  is None:
        result.append(root.value)
    dfs(root.lchild,result)
    dfs(root.rchild,result)


'''迭代法需要借助栈这个数据结构, 然后模拟遍历树的过程中的进栈出栈过程. 
其实在 DFS 的方法中, 编程语言就已经把栈的调用帮你做好了
递归之所以能实现，是因为函数的每个执行过程都在栈中有自己的形参和局部变量的拷贝
'''
def bfs(root, result):
    stack = []
    current = root
    while current is not None or len(stack) > 0:
        # 相当于递归法中的 dfs(root.left), 优先把left节点都压入栈
        while current:
            stack.append(current)
            current = current.lchild
        # left 节点都已经压完了, 从栈中取最近压入的 TreeNode
        current = stack.pop()
        if current.lchild is None and current.rchild is None:
            result.append((current.value))
        # 相当于递归法中的 dfs(root.right) 那一步
        current = current.rchild

def main():  # Main function for testing.
    root1 = TreeNode(3)
    root1.lchild = TreeNode(5)
    root1.rchild = TreeNode(1)
    root1.lchild.lchild=TreeNode(6)
    root1.lchild.rchild=TreeNode(2)
    root1.rchild.lchild=TreeNode(9)
    root1.rchild.rchild=TreeNode(8)
    root1.lchild.rchild.lchild=TreeNode(7)
    root1.lchild.rchild.rchild=TreeNode(4)

    root2 = TreeNode(3)
    root2.lchild = TreeNode(5)
    root2.rchild = TreeNode(1)
    root2.lchild.lchild=TreeNode(6)
    root2.lchild.rchild=TreeNode(7)
    root2.rchild.lchild=TreeNode(4)
    root2.rchild.rchild=TreeNode(2)
    root2.rchild.rchild.lchild=TreeNode(9)
    root2.rchild.rchild.rchild=TreeNode(8)

    # 找出叶序列相同则print true，否则就false

    '''自己的思路：后序遍历加add list'''
    tree_postorder_list1 = []
    tree_postorder_list2 = []
    leaf_list1 = postorder_travel(root1,tree_postorder_list1)
    leaf_list2 = postorder_travel(root2,tree_postorder_list2)
    print(leaf_list1)
    print(leaf_list2)
    if leaf_list1 == leaf_list2:
        print('true')
    elif leaf_list1 != leaf_list2:
        print('false')

    '''答案：DFS与BFS'''

    # DFS
    res1 = []
    res2 = []
    dfs(root1,res1)
    dfs(root2,res2)
    print(res1,res2)
    if(res1 == res2):print('true')
    else: print('false')

    # BFS
    res1 = []
    res2 = []
    bfs(root1,res1)
    bfs(root2,res2)
    print(res1,res2)
    if(res1 == res2):print('true')
    else: print('false')





if __name__ == "__main__":
    main()