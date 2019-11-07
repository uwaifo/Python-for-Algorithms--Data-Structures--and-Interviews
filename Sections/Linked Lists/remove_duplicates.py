'''
Docker, Jenkins, Kubernetes, Ansible, Terraform, Python, Bash, Shell 
Given a sorted linked list, delete all duplicates such that each element appear only once.
Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d

print(c.val)


class Solution(object):
    def deleteDuplicates(self, head):
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        