

#
# Complete the 'removeDuplicates' function below.
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

def removeDuplicates(llist):
    
    current = llist
    while (current is not None and current.next is not None):
        if (current.next.data == current.data):
            nextNode = current.next
            current.next = nextNode.next
            nextNode.next = None
            del nextNode
        else:
            current = current.next
    
    return llist

