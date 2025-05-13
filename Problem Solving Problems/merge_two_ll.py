

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    
    head = SinglyLinkedListNode(0)
    headNode = head
    
    while (head1 is not None and head2 is not None):
        if (head1.data <= head2.data):
            head.next = SinglyLinkedListNode(head1.data)
            head1 = head1.next
        else:
            head.next = SinglyLinkedListNode(head2.data)
            head2 = head2.next
        head = head.next
    
    while (head1 is not None):
        head.next = SinglyLinkedListNode(head1.data)
        head1 = head1.next
        head = head.next
    
    while (head2 is not None):
        head.next = SinglyLinkedListNode(head2.data)
        head2 = head2.next
        head = head.next
        
    headNode = headNode.next
    return headNode

