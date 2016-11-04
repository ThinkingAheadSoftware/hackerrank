"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""
# https://www.hackerrank.com/challenges/ctci-linked-list-cycle

def has_cycle(head):
    node = head.next
    passed_list = []
    while node is not None:
        passed_list.append(node)
        node = node.next
        if node in passed_list:
            return True
    return False
