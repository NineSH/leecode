# 合并两个已排序的链接列表并将其作为新列表返回。新列表应该通过拼接前两个列表的节点来完成。
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
class ListNode(object):
    '''
     data: 节点保存的数据
     _next: 保存下一个节点对象
     '''
    def __init__(self,x,prev=None):
        self.val=x
        self.next=prev
    def __repr__(self):
        '''
        用来定义Node的字符输出，
        print为输出data
        '''
        return str(self.val)
###########单链表实现
class chain(object):
    #初始化
    def __init__(self):
        self.head=None
        self.length=0
    ##判空
    def isEmpty(self):
        return self.length==0
    ##链表结尾插入
    def append(self,item):
        if isinstance(item,ListNode):
            node=item
        else:
            node=ListNode(item)
        if self.head==None:
            self.head=node
        else:
            be_node=self.head
            while be_node.next:
                be_node=be_node.next
            be_node.next=node
        self.length+=1

    #插入数据
    def insert(self,index,item):
        if self.isEmpty():
            print('this chain table is empty')
            return  None
        if index<0 or index >=self.length:
            print('error:out of index')
            return None
        in_node=ListNode(item)
        node=self.head
        count=1

        while True:
            node=node.next
            count+=1
            if count==index:
                next_node=node.next
                node.next=in_node
                self.length+=1
                return

    ##删除数据
    def delete(self,index):
        if self.isEmpty():
            print('this chain table is empty')
            return
        if index<0 or index>=self.length:
            print("error:out of index")
            return
        if index==0:
            self.head=self.head.next
            self.length-=1
            return
        j=0
        node=self.head
        prev=self.head
        while node.next and j<index:
            prev=node
            node=node.next
            j+=1
        if j==index:
            prev.next=node.next
            self.length-=1

    ###链表初始化
    def initlist(self,data):
        self.head=ListNode(data[0])
        p=self.head
        for i in data[1:]:
            node=ListNode(i)
            p.next=node
            p=p.next
#########合并两个已经排序的链接列表  iteratively 迭代形式
def mergeTwoLists1(l1,l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    merge=curr=ListNode(0)
    while l1 and l2:
        if l1.val<l2.val:
            curr.next=l1
            l1=l1.next
        else:
            curr.next=l2
            l2=l2.next
        curr=curr.next
    curr.next=l1 or l2
    return merge.next

##递归
def mergeTwoLists2(l1,l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val<l2.val:
        l1.next=mergeTwoLists2(l1.next,l2)
        print(l1)
        return l1
    else:
        l2.next=mergeTwoLists2(l1,l2.next)
        print(l2)
        return l2
if __name__=="__main__":
    l1=ListNode('1',(ListNode('2',(ListNode('4')))))
    # while True:
    #     print(l1.val)
    #     if l1.next!=None:
    #         l1=l1.next
    #     else:
    #         break
    l2=ListNode('1',(ListNode('3',(ListNode('4')))))
    print(mergeTwoLists1(l1,l2))
    # while True:
    #     print(l3.val)
    #     if l3.next!=None:
    #         l3=l3.next
    #     else:
    #         break
    mergeTwoLists2(l1,l2)

