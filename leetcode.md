# Leetcode

https://blog.csdn.net/tinkle181129/article/details/79326023

## 19.09.26

### 1. 删除链表中重复的结点

https://www.nowcoder.com/practice/fc533c45b73a41b0b44ccba763f866ef?tpId=13&tqId=11209&tPage=3&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

>
>题目描述
>在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

#### Method1

```
class Solution:
 
    def deleteDuplication(self, pHead):
 
        if pHead is None or pHead.next is None: # 只有一个节点或两个节点的情况
            return pHead
         
        vHead = ListNode(0)
        vHead.next = pHead      # 添加虚拟节点指向头节点
         
        p = vHead
        q = vHead.next
         
        while q is not None:    # 注意要判空
            if q.next is not None and q.val==q.next.val:            # 在先对 q.next 判断之后再对 q.next 取 val
                while q.next is not None and q.val == q.next.val:   # 虽然之前已经判断过 q.next，但是在while循环中修改了 q 的值，因此这里对 q.next 的判空也是必要的
                    q = q.next
                p.next = q.next
                q = q.next
            else:
                p = p.next
                q = q.next
        return vHead.next
```

1. 添加一个虚拟节点vHead。因为删除链表中的元素是修改指针，如果要删除第二个元素，那么就需要修改第一个元素的指针。
2. 有两个指针，一个p，一个q。p指向扫过的元素中最后一个确定不重复的元素。而q是工作指针。
3. 判断元素是否重复时可以只用 q 来判断。不需要同时使用 p，q。


### 2. 斐波那契数列

不可取的做法：直接使用 f(n+1) = f(n) + f(n-1) 递归。这样当n比较大的时候效率很低。
因为大量的重复计算。

#### Method1

不采用递归的思想从大到小计算，而是采用普通的迭代的思想，从小到大计算。

直观的想法

```
class Solution:
    def Fibonacci(self, n):
        f0 = 0
        f1 = 1
        result = 0
        if n == 0:
            return f0
        if n == 1:
            return f1
        for i in range(n-1):
            result = f0 + f1
            f0 = f1
            f1 = result
        return result
```

上面的方法中使用了三个变量。实际上有两个变量就可以解决，下面是 pythonic的写法：


```
class Solution:
    def Fibonacci(self, n):
        f0 = 0
        f1 = 1
        for i in range(n):
            f0, f1 = f1, f0 + f1
        return f0
```

这种写法比上面的写法的好处是 1. 不需要进行边界条件的判断 2. 充分利用了python的语言特性。

#### Method2 未完。之后看动态规划。


## 09.27

### 链表反转

- [反转链表__牛客网](https://www.nowcoder.com/questionTerminal/75e878df47f24fdc9dc3e400ec6058ca)

>输入一个链表，反转链表后，输出新链表的表头。

#### Method1

```
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        p = None
        q = pHead
        if q is None:
            return None
        else:
            r = q.next
            while q is not None:
                q.next = p
                p = q
                q = r
                r = r.next if r is not None else None
            return p
```

注意有三个指针。

![](/Users/ed/PycharmProjects/leetcode/images/IMG_C5BCA10C8143-1.jpeg)

#### Method2 

递归？如何写？

