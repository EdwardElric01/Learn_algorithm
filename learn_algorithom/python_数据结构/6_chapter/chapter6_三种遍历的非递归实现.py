
# 非递归实现三种遍历（自法）

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():

    # 先根序
    def preorder_non_recrusive(self, tree, func):
        st = [] # 用列表来模拟栈
        st.append((tree, 0))
        while len(st) > 0:
            tree, status = st.pop()
            if tree is not None:
                if status==0:
                    st.append((tree.right, 0))
                    st.append((tree.left, 0))
                    st.append((tree, 1))
                else:
                    func(tree.val)

    # 中根序
    def midorder_non_recrusive(self, tree, func):
        st = [] # 用列表来模拟栈
        st.append((tree, 0))
        while len(st) > 0:
            tree, status = st.pop()
            if tree is not None:
                if status==0:
                    st.append((tree.right, 0))
                    st.append((tree, 1))
                    st.append((tree.left, 0))
                else:
                    func(tree.val)

    # 后根序
    def postorder_non_recrusive(self, tree, func):
        st = [] # 用列表来模拟栈
        st.append((tree, 0))
        while len(st) > 0:
            tree, status = st.pop()
            if tree is not None:
                if status==0:
                    st.append((tree, 1))
                    st.append((tree.right, 0))
                    st.append((tree.left, 0))
                else:
                    func(tree.val)

def test():

    tree = TreeNode('A')
    tree.left = TreeNode('B')
    tree.left.left = TreeNode('D')
    tree.left.left.right= TreeNode('H')
    tree.left.right = TreeNode('E')
    tree.left.right.right = TreeNode('I')

    tree.right = TreeNode('C')
    tree.right.left = TreeNode('F')
    tree.right.right = TreeNode('G')
    tree.right.left.left = TreeNode('J')
    tree.right.left.right = TreeNode('K')

    solution = Solution()
    print('preorder: ', end="")
    solution.preorder_non_recrusive(tree, lambda x: print(x, end=""))

    print('\nmidorder: ', end="")
    solution.midorder_non_recrusive(tree, lambda x: print(x, end=""))

    print('\npostorder: ', end="")
    solution.postorder_non_recrusive(tree, lambda x: print(x, end=""))


if __name__ == '__main__':

    test()

