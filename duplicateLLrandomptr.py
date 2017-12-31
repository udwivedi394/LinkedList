class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		self.random = None

#Time Complexity: O(n)
#Space Complexity: O(n)
def duplicateLL(root):
	prevNode = None
	temp = root
	dhead = None
	lookup = {}

	#Create corresponding nodes for every Node in LL
	while temp or prevNode:
		if prevNode:
			#If prevNode exists then create new Node with corresponding data and connect
			#the next of prevNode to newNode
			prevNode.next = Node(prevNode.data)
			
			#Save the Head of the new linked list
			if dhead==None:
				dupNode = dhead = prevNode.next
			#Connect the Node of previous Node in New Linked List to newly created Node
			else:
				dupNode.next = prevNode.next
				dupNode = dupNode.next

			#Store the mapping in Hashmap as, {newNode: corresponding_original_node}
			lookup[dupNode] = prevNode

		#Set the current Node as prevNode
		prevNode = temp
		#Move temp to next
		if temp:
			temp = temp.next	

	temp = dhead

	#Connect the random of newNode to next of random of corresponding node in original Node
	while temp:
		orgNode = lookup[temp]
		temp.random = orgNode.random.next
		temp = temp.next

	#Restore the connections in original LL
	temp = dhead
	while temp:
		orgNode = lookup[temp]
		if temp.next:
			orgNode.next = lookup[temp.next]
		else:
			orgNode.next = None
		temp = temp.next

	return dhead

def llTraversal(root):
	temp = root
	while temp:
		print temp.data,"->",
		temp = temp.next
	print "None"

	temp = root
	while temp:
		print temp.random.data,"->",
		temp = temp.next
	print "None"
	return

h1 = root = Node(1)
h2 = root.next = Node(2)
h3 = root.next.next = Node(3)
h4 = root.next.next.next = Node(4)
h5 = root.next.next.next.next = Node(5)

h1.random = h3
h2.random = h1
h3.random = h5
h4.random = h3
h5.random = h2

print "Orginal LL"
llTraversal(root)
dHead = duplicateLL(root)

print "New LL"
llTraversal(dHead)

print "Original New LL"
llTraversal(root)
