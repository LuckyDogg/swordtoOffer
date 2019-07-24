import sys


class LinkNode:
    """
    链表节点的创建
    """
    def __init__(self, val: int):
        self.value = val
        self.next = None

    def insert(self, next_node):
        self.next = next_node
        return self.next

    def delete(self):
        self.next = self.next.next

    def __str__(self):
        return self.value


head = LinkNode(1)
var = head
listvalue = [2, 3, 4, 5, 6]
for i in listvalue:
    var = var.insert(LinkNode(i))


class Solution:
    @staticmethod
    def print_list_tail2head(headnode: LinkNode):
        """
        递归的方法实现
        :param headnode:
        :return:
        """
        if headnode is not None:
            Solution.print_list_tail2head(headnode.next)
            print(headnode.value, end=' ')

    @staticmethod
    def print_list_tail2head_by_stack(headnode: LinkNode):
        varnode = headnode
        nodestack = []
        while varnode is not None:
            nodestack.append(varnode)
            varnode = varnode.next
        while len(nodestack) > 0:
            print(nodestack.pop().value)


if __name__ == '__main__':
    argv1 = sys.argv[1]
    print(argv1)
    if argv1 == 'stack':
        Solution.print_list_tail2head_by_stack(head)
    else:
        Solution.print_list_tail2head(head)






