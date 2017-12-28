class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

#This function only detects if there is loop in LL
#Time Complexity: O(n), Space: O(1)
def detectLoop(root):
	temp = root
	hunter = root

	while temp and hunter and hunter.next:	
		hunter = hunter.next.next
		if temp == hunter:
			print "Loop found!!"
			break
		temp = temp.next
	return hunter

#This function takes HEAD of ll and any of the loop node as parameters
def removeLoop(root,loopNode):
	temp1 = root

	while 1:
		temp2 = loopNode
		while temp2.next != loopNode and temp2.next != temp1:
			temp2 = temp2.next
		if temp2.next == temp1:
			print "In the name of Holy Lord!, I'm Removing the Loop!!"
			temp2.next = None
			break
		temp1 = temp1.next
	return root

#Better Solution than removeLoop, because we need to traverse through loop only 2 time in this case
#Ist when counting the number of nodes in Loop
#2nd when going for the removal of loop
def removeLoop02(root,loopNode):
	temp1 = root
	temp2 = loopNode

	countNodesinLoop = 0
	while temp2.next != loopNode:
		countNodesinLoop += 1
		temp2 = temp2.next
	
	temp2 = root
	while countNodesinLoop:
		temp2 = temp2.next
		countNodesinLoop -= 1

	while temp2.next != temp1:
		temp2 = temp2.next
		temp1 = temp1.next

	temp2.next = None
	return root

def llTraversal(root):
	temp = root
	i = 15
	while temp and i:
		print temp.data,"->",
		temp = temp.next
		i -= 1
	print "None"
	return

root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
temp1=root.next.next.next.next = Node(5)
temp1.next = Node(6)
temp1.next.next = Node(7)
loop = temp1.next.next.next = Node(8)
loop.next = root.next.next

loopNode=detectLoop(root)
llTraversal(root)
removeLoop02(root,loopNode)
llTraversal(root)
