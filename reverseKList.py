import time

class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

def reverseKList(root,k):

    headFound = False
    count = 0
    temp = curHead = root
    prevHead = None


    while temp:
        count += 1
        #print "In:",count,"temp.val:",temp.val
        if count == k:
            #save the next linkage
            nextNode = temp.next

            #break the further link
            temp.next = None

            #Reverse the LL, return the new Head
            tt = reverseLL(curHead)
            traverseLL(tt)

            #time.sleep(10)
            if headFound == False:
                root,headFound = tt,True

            temp2 = tt
            while temp2.next:
                temp2 = temp2.next
            temp = curHead = temp2.next = nextNode

            if prevHead != None:
                prevHead.next = tt
            #store the end of last list
            prevHead = temp2

            count = 0
        else:
            temp = temp.next

    return root

def reverseLL(root):
    temp = root
    prev = None
    while temp:
        nextNode = temp.next
        if nextNode == None:
            root = temp
        temp.next = prev
        prev = temp
        temp = nextNode
    return root

def traverseLL(temp):
    while temp:
        print temp.val,"->",
        temp = temp.next
    print "None"

root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
temp = root.next.next.next.next = Node(5)
temp.next = Node(6)

root = reverseKList(root,2)
traverseLL(root)
