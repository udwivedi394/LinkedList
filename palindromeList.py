class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def palindromeList(root):
    count = 0
    temp = root
    while temp:
        count += 1
        temp = temp.next

    temp = root
    i = 0
    while i < count/2:
        temp = temp.next
        i += 1

    back = reverseList(temp)
    traverseLL(root)
    traverseLL(back)

    temp1,temp2 = root,back
    
    while temp1 and temp2:
        if temp1.data != temp2.data:
            return False
        temp1 = temp1.next
        temp2 = temp2.next
    return True

def reverseList(ll):
    temp = head = ll
    prev = None

    while temp:
        if temp.next == None:
            head = temp
        next_node = temp.next
        temp.next = prev
        prev = temp
        temp = next_node

    return head

def traverseLL(head):
    temp = head
    while temp:
        print temp.data,"->",
        temp = temp.next
    print "None"

root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(2)
root.next.next.next.next = Node(1)
#root.next.next.next.next.next = Node(1)


#traverseLL(root)
#root = reverseList(root)
traverseLL(root)

print palindromeList(root)
