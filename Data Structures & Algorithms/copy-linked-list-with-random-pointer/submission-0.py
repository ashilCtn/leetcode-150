"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashMap = {None : None}

        cur = head
        while cur:
            node = Node(cur.val)
            hashMap[cur] = node
            cur = cur.next
        
        temp = head
        while temp:
            cur = hashMap[temp]
            cur.next = hashMap[temp.next]
            cur.random = hashMap[temp.random]
            temp = temp.next
        
        return hashMap[head]