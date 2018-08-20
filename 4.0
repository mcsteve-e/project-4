'''
        Author:  McSteve Ezikeoha
        Title:   Binary Search Trees
        Date:    April 25, 2018
'''

# The BST Property is defined as the following:
#       Given node N,
#       if N has no children, return True
#       if N.left exists and if N.left.payload > N.payload return false
#       if N.right exists and if N.right.payload < N.payload return false
#       if N.left exists and if N.left is not a BST return false
#       if N.right exists and if N.right is not a BST return false
#       if you make it this far, return true!

class BST:
	class Node:
		def __init__(self, payload):
			self.payload = payload
			self.left = None
			self.right = None

	def __init__(self):
		self.root = None

	def prettyprint(self):
		BST.prettyprint_aux(self.root, 0)

	def prettyprint_aux(somenode, indentLevel):
		if somenode.right != None: 
			BST.prettyprint_aux(somenode.right, indentLevel+1)
		for k in range(indentLevel):
			print("    ", end="")
		print(somenode.payload)
		print()
		if somenode.left != None: 
			BST.prettyprint_aux(somenode.left, indentLevel+1)

	def find(self, target):
		return BST.find_aux(self.root, target)

	def find_aux(treeptr, target):
		if treeptr == None:
			return None
		if treeptr.payload == target:
			return treeptr
		elif target < treeptr.payload:
			return BST.find_aux(treeptr.left, target)
		else:      # look in right subtree
			return BST.find_aux(treeptr.right, target)

	def attach_in_order(self, new_value):
		if self.root == None:
			self.root = BST.Node(new_value)
		else:
			BST.attach_in_order_aux(self.root, new_value)

	def attach_in_order_aux(treeptr, new_value):
		pass
		#  if new_value is less than treeptr's payload, 
		#             if the left child is None then add a new node as left child
		#             else go down the left child subtree
		#  else do the same on the right side

	def flip(self):
		flip_aux(self.root)

	def flip_aux(some_node):
		pass
		

if __name__ == "__main__":
	tree = BST()
	tree.root = BST.Node("man")
	somenode = tree.find("man")
	somenode.left = BST.Node("dog")
	somenode.right = BST.Node("zebra")
	tree.prettyprint()
