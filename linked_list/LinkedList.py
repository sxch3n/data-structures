class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt


class LinkedList:
    def __init__(self,*args):
        self.LL = self.buildLL(*args)

    def buildLL(self,*args):
        if not args:
            return None
        node_queue = []
        for val in args:
            node_queue.append(Node(val))
        
        if node_queue:
            head = node_queue.pop(0)
            curr = head
        while node_queue:
            curr.nxt = node_queue.pop(0)
            curr = curr.nxt
        return head

    def getLL(self):
        return self.LL

    def reverse(self):
        head = self.LL
        if not head:
            return None
        dh = Node(None)
        while head:
            if not dh.nxt:
                tmp_node = head.nxt
                head.nxt = None
                dh.nxt = head                
                head = tmp_node
            else:
                tmp_node = head.nxt
                head.nxt = dh.nxt
                dh.nxt = head
                head = tmp_node
        return dh.nxt
    
    def removeKthFromEnd(self,n):
        head = self.LL
        count = 0
        dh = Node(None)
        dh.next = pointer = curr = head
        while curr.next:
            curr = curr.next
            if count>=n:
                pointer = pointer.next
            count += 1
        if count<n:
            dh.next = dh.next.next
        else:
            pointer.next = pointer.next.next
        return dh.next
       
def main(*args):
    LL = LinkedList(*args).getLL()
    while LL:
        print(LL.val)
        LL = LL.nxt
    reversedLL = LinkedList(*args).reverse()
    while reversedLL:
        print(reversedLL.val)
        reversedLL = reversedLL.nxt
if __name__ == "__main__":
    main(1, 2, 3, 4)

