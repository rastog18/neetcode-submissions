# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def createRecursiveNode(i):
            if i < 0:
                return None
            newNode = ListNode(num1[i], None)
            newNode.next = createRecursiveNode(i-1)
            return newNode
        
        itr = l1
        num1 = 0
        i = 0
        while(itr):
            num1 += (itr.val * 10**i)
            itr = itr.next
            i+=1

        itr = l2
        i = 0
        num2 = 0
        while(itr):
            num1 += itr.val * 10**i
            itr = itr.next
            i+=1

        num1 += num2
        num1 = str(num1)

        return createRecursiveNode(len(num1)-1)


        """itr = l1
        itr2 = l2
        carry = 0
        dummy = ListNode(0, None)
        prev = None

        while(itr or itr2):
            if itr and itr2:
                value = itr.val + itr2.val 
            elif itr:
                value = itr.val
            else: 
                value = itr2.val

            setValue = (value + carry) %10
            carry = (value + carry) // 10

            node = ListNode(setValue, None)

            if prev:
                prev.next = node
            else:
                dummy.next = node
            prev = node

            if itr:
                 itr = itr.next
            if itr2:
                itr2 = itr2.next
        
        if carry:
            node = ListNode(carry, None)
            prev.next = node
        return dummy.next"""
        
            