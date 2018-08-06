INF = 10**8
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def partitionList(A,x):
    head = temp = ListNode(INF)
    temp.next = A
    
    markerHead,marker = None,None
    while temp.next:
        if temp.next.val < x:
            if markerHead == None:
                markerHead = marker = temp.next
            else:
                marker.next = temp.next
                marker = marker.next
            temp.next = temp.next.next
            marker.next = None
        else:
            temp = temp.next

    final = None
    if markerHead:
        marker.next = head.next
        final = markerHead
    else:
        final = head.next
    #traverse(markerHead)
    return final


def traverse(temp):
    while temp:
        print temp.val,"->",
        temp = temp.next
    print "None"

A = [1,4,3,2,5,2]
X = 5

A = [10,15,11,9,8,3,2,14,12]
X = 15

A = [1]
X = 1

temp = root = ListNode(A[0])
for i in A[1:]:
    temp.next = ListNode(i)
    temp = temp.next

#traverse(root)
root = partitionList(root,X)
traverse(root)
