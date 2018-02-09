class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def reorderList(A):
    count = 0
    temp = A
    while temp:
        count += 1
        temp = temp.next

    i = 1
    temp = A
    while i < round(count/2.0+0.1):
        temp = temp.next
        i += 1

    #print temp.val
    nextNode = temp.next
    temp.next = None

    prevNode = head2 = None
    temp2 = nextNode
    while temp2:
        if temp2.next == None:
            head2 = temp2

        nextNode = temp2.next
        temp2.next = prevNode
        prevNode = temp2
        temp2 = nextNode

    temp2 = head2
    temp1 = A

    while temp2 and temp1:
        nextNode1 = temp1.next

        nextNode2 = temp2.next
    
        temp1.next = temp2
        temp2.next = nextNode1

        temp1 = nextNode1
        temp2 = nextNode2

    return A

def traverseLL(temp):
    while temp:
        print temp.val,"->",
        temp = temp.next
    print "None"

A = [i for i in range(1,9)]

root = temp = ListNode(A[0])

for i in A[1:]:
    temp.next = ListNode(i)
    temp = temp.next

traverseLL(root)
root = reorderList(root)
traverseLL(root)
