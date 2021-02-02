class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0
    
    def append(self,node):
        if (self.head == None):
            self.head = node
        else:
            curn = self.head
            while (curn.next != None):
                curn = curn.next
            curn.next = node
    
    def getDataIndex(self, data):
        curn = self.head
        idx = 0
        while (curn):
            if (curn.data == data):
                return idx
            curn = curn.next
            idx += 1
        return -1

    def insertNodeAtIndex(self,idx,node):
        curn = self.head
        prevn = None
        cur_i = 0

        if idx == 0 :
            if self.head:
                nextn = self.head
                self.head = node
                self.head.next = nextn
            else:
                self.head = node
        else:
            while cur_i < idx:
                if curn:
                    prevn = curn
                    curn = curn.next
                else:
                    break
                cur_i += 1
            if cur_i == idx:
                node.next = curn
                prevn.next = node
            else:
                return -1

    def insertNodeAtData(self,data,node):
        idx = self.getDataIndex(data)
        if idx>=0:
            self.insertNodeAtIndex(idx,node)
        else:
            return -1

    def deleteAtIndex(self,idx):
        curn_i = 0
        curn = self.head
        prevn = None
        nextn = self.head.nextn

        if idx == 0:
            self.head = nextn
        else:
            while curn_i < idx:
                if curn.next:
                    prevn = curn
                    curn = nextn
                    nextn = nextn.nextn
                else:
                    break
                curn_i += 1
            if curn_i == idx:
                prevn.next = nextn
            else:
                return -1

    def clear(self):
        self.head = None
    
    def print(self):
        curn = self.head
        string = ""

        while curn:
            string += str(curn.data)
            if curn.next:
                string += "->"
            curn = curn.next
        print (string)
        
    def reverseNode(self):
        #반복 구조
        curn = self.head
        prevn = None

        while(curn):
            nextn, curn.next = curn.next, prevn
            prevn,curn = curn, nextn

        self.head=prevn


    # def reverseNode(self,curn:Node,prevn:Node=None):
    #     #재귀구조
    #     nextn = curn.next
    #     if not curn:
    #         self.head=prevn
    #         return self
    #     nextn = curn.next
    #     curn.next = prevn
    #     return self.reverseNode(nextn,curn)

#print(reverse(1->2->3->4->5->NULL))

if __name__=="__main__":
    sl = SinglyLinkedList()
    sl.append(Node(1))
    sl.append(Node(2))
    sl.append(Node(3))
    sl.append(Node(4))
    sl.append(Node(5))
    sl.append(None)
    sl.print()

    sl.reverseNode()
    sl.print()



# def reverse(node,prev):
#     if not node:
#         return prev
#     next, node.next = node.next, prev

#     return reverse(next,node)

# print(reverse(1->2->3->4->5->NULL))