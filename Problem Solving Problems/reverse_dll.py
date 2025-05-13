

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts INTEGER_DOUBLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def reverse(llist):
    
    previous = None
    current = llist
    forward = None
    
    while current is not None:
        forward = current.next
        current.next = previous
        current.prev = forward
        previous = current
        current = forward
    
    return previous

