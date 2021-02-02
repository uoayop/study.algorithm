#요세푸스 문제
#https://www.acmicpc.net/problem/1158

import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class CircleLinkedList:
    def __init__(self):
        self.head = Node(1)
        self.tail = None

    def __str__(self):
        print_list = '< '
        node = self.head
        while True:
            print_list += str(node)
            if node == self.tail:
                break
            node = node.next
            print_list += ', '
        print_list += ' >'
        return print_list

    def insertFirst(self, data):
        new_node = Node(data)
        if self.tail == None:
            self.tail = self.head
        temp_node = self.head
        self.head = new_node
        self.head.next = temp_node
        self.tail.next = new_node

    def insertByIndex(self, num, data):
        node = self.selectNodeByIndex(num)
        new_node = Node(data)
        temp_next = node.next
        node.next = new_node
        new_node.next = temp_next

    def insertLast(self, data):
        new_node = Node(data)
        if self.tail == None:
            self.tail = new_node
            self.head.next = self.tail
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.tail.next = self.head

    def selectNodeByIndex(self, num):
        node = self.head
        count = 0
        while count < num:
            node = node.next
            count += 1
        return node

    def selectNodeByData(self,item):
        node = self.head
        if node:
            return
        while node.data != item:
            node = node.next
        return node

    def selectPreviousNodeByData(self,item):
        node = self.head
        while node.next.data != item:
            node = node.next
        return node

    def deleteNodeByIndex(self, num):
        if num == 0:
            self.deleteHead()
            return
        node = self.selectNodeByIndex(num - 1)
        node.next = node.next.next
        del_node = node.next
        del del_node

    def deleteNodeByData(self, item):
        prev_node = self.selectPreviousNodeByData(item)
        prev_node.next = prev_node.next.next

    def deleteHead(self):
        node = self.head
        self.head = node.next
        del node

    


n, k = (map(int,sys.stdin.readline().rstrip().split()))
result=[]

if n==1:
    print("<1>")

else:
    m_list = CircleLinkedList()

    for i in range(2,n+1):
        m_list.insertLast(i)

    node = m_list.head
    for i in range(n):
        if i==0:
            for j in range(k-1):
                node=node.next
        else:
            for j in range(k):
                node=node.next

        result.append(node.data)
        m_list.head = node.next
        m_list.deleteNodeByData(node.data)

    print("<"+", ".join(str(e) for e in result)+">")
