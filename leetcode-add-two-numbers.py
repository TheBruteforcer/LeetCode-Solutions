# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        l1.reverse()
        l2.reverse()
        num1 = ''
        num2 = ''
        for x in l1:
            num1 +=str(x)
        for z in l2:
            num2 +=str(z)
        eq = [x for x in str(int(num1) + int(num2))]
        eq.reverse()
        return eq 
print(Solution.addTwoNumbers(Solution, [1,2,3], [2,3,4]))