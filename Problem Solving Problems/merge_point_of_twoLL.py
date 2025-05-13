

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    
    occurance = {}
    while head1 is not None:
        occurance[head1] = True
        head1 = head1.next
        
    while head2 is not None:
        if head2 in occurance.keys():
            return head2.data
        head2 = head2.next

