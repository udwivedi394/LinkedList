class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def reversemnLL(A,m,n):
    i = 0

    temp = root = A
    startPrevNode = tail = None

    prevNode = None
    while temp:
        i += 1
        if i == m-1:
            startPrevNode = temp
    
        if i >= m and i <= n:
            if prevNode == None:
                tail = temp
            nextNode = temp.next
            temp.next = prevNode
            prevNode = temp
            temp = nextNode

        else:
            temp = temp.next

    if m!=1:
        startPrevNode.next = prevNode
    else:
        root = prevNode
    tail.next = nextNode
    return root 

def reversemnLL02(A,m,n):
    i = 0

    temp = root = A
    startPrevNode = endNextNode = None

    start = None
    while temp:
        i += 1
        if i == m-1:
            startPrevNode = temp
    
        if i == m:
            start = temp
            if m!=1:
                startPrevNode.next = None

        elif i == n:
            endNextNode = temp.next
            temp.next = None
        temp = temp.next

    tail = start
    start = reverseLL(start)

    traverseLL(start)
    if m!=1:
        startPrevNode.next = start
    else:
        root = start
    tail.next = endNextNode

    return root 

def reverseLL(root):
    temp = root
    prevNode = head = None

    while temp:
        if temp.next == None:
            head = temp

        nextNode = temp.next
        temp.next = prevNode

        prevNode = temp
        temp = nextNode

    return head

def traverseLL(temp):
    while temp:
        print temp.val,"->",
        temp = temp.next
    print "None"

A = [i for i in range(1,10)]

root = temp = ListNode(A[0])

for i in A[1:]:
    temp.next = ListNode(i)
    temp = temp.next

traverseLL(root)
root = reversemnLL(root,5,9)
traverseLL(root)
