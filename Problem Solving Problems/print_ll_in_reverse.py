

#
# Complete the 'reversePrint' function below.
#
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

def reversePrint(llist):
    
    if llist is not None:
        previous = None
        current = llist
        forward = None
        
        while current is not None:
            forward = current.next
            current.next = previous
            previous = current
            current = forward
        
        while previous is not None:
            print(previous.data)
            previous = previous.next

