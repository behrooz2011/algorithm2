class ListNode:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next
class LinkedList:
    #convert to Linked List
    def to_LL(self,arr):
        dummy = ListNode()
        curr = dummy
        for value in arr:
            curr.next = ListNode(value)
            curr = curr.next
        return dummy.next
    #convert to array
    def to_arr(self,node):
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        return arr
ll1 = LinkedList()
node = ll1.to_LL([2,3,1,4])
print(ll1.to_arr(node))
print(node.val)
    