"""138. Copy List with Random Pointer
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        dict = {}
        old_head = head
        new_head = RandomListNode(old_head.label)
        dict[old_head] = new_head
        old = head.next
        new = new_head
        while old:
            node = RandomListNode(old.label)
            dict[old] = node
            new.next = node
            new = new.next
            old = old.next
        old = old_head
        new = new_head
        while new:
            if old.random:
                new.random = dict[old.random]
            new = new.next
            old = old.next
        return new_head
