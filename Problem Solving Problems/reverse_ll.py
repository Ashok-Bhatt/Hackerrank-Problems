

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reverse(llist):
    
    previous = None
    current = llist
    forward = None
    
    while (current is not None):
        forward = current.next
        current.next = previous
        previous = current
        current = forward
    
    return previous

