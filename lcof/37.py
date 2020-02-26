# -*- coding: utf-8 -*-
# @Time    : 2020/2/26 上午9:44
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 37.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def __init__(self):
        self.data = []
        self.pos = 0

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.data = []
        self.encode(root)
        result = ''
        for x in self.data:
            if result:
                result += ','
            if x is None:
                result += 'null'
            else:
                result += str(x)
        return result

    def encode(self, node):
        if not node:
            self.data.append(None)
            return
        self.data.append(node.val)
        self.encode(node.left)
        self.encode(node.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.data, self.pos = [], 0
        temp = data.split(',')
        for x in temp:
            if x == 'null':
                self.data.append(None)
            else:
                self.data.append(int(x))
        return self.decode()

    def decode(self):
        if self.data[self.pos] is None:
            self.pos += 1
            return None
        node = TreeNode(self.data[self.pos])
        self.pos += 1
        node.left = self.decode()
        node.right = self.decode()
        return node


if __name__ == '__main__':
    obj = Codec()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    data = obj.serialize(root)
    print(data)
    obj.deserialize(data)
