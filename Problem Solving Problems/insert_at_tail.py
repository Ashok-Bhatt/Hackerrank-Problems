

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    
    newNode = SinglyLinkedListNode(data)
    
    if head is None:
        return newNode
    
    temp = head
    while (temp.next is not None):
        temp = temp.next
    
    temp.next = newNode
    return head

