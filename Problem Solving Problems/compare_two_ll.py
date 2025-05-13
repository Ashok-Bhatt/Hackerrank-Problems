

# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    
    head1 = llist1
    head2 = llist2
    
    while True:
        if (head1 is None and head2 is None):
            return True
        elif (head1 is None or head2 is None):
            return False
        elif (head1.data == head2.data):
            head1 = head1.next
            head2 = head2.next
        else:
            return False

