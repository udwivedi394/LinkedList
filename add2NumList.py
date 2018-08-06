class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

def add2NumList(A,B):
    
    carry = 0
    tempA,tempB = A,B

    countA = countB = 0
    while tempA and tempB:
        val = tempA.val + tempB.val
        tempB.val = tempA.val = (val+carry)%10
        carry = (val+carry)/10

        tempA = tempA.next
        tempB = tempB.next

        countA = countB = countA+1

    while tempA:
        val = tempA.val
        tempA.val = (val+carry)%10
        carry = (val+carry)/10
        tempA = tempA.next
        countA += 1

    while tempB:
        val = tempB.val
        tempB.val = (val+carry)%10
        carry = (val+carry)/10
        tempB = tempB.next
        countB += 1

    last = None
    if carry != 0:
        last  = Node(carry)

    if countA > countB:
        final=A
    else:
        final=B

    temp = final
    while temp.next:
        temp = temp.next
    temp.next = last

    temp = final
    trailZero = False
    marker = None

    while temp.next:
        if trailZero==False and temp.next.val == 0:
            trailZero = True
            marker = temp
        
        if trailZero and temp.next.val != 0:
            trailZero = False
            marker = None
        temp = temp.next

    if marker:
        marker.next = None

    return final

def traverse(temp):
    while temp:
        print temp.val,"->",
        temp = temp.next
    print "None"

A = Node(9)
A.next = Node(9)
A.next.next = Node(1)

B = Node(1)
#B.next = Node(6)
#B.next.next = Node(7)
#B.next.next.next = Node(0)
#B.next.next.next.next = Node(0)
#B.next.next.next.next.next = Node(0)

root = add2NumList(A,B)
traverse(root)
