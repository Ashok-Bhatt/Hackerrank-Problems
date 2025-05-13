

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    
    occurance = {}
    
    while (head is not None):
        if (head in occurance.keys()):
            return 1
        occurance[head] = True
        head = head.next
    
    return 0

