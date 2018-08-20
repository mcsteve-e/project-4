'''
        Author:  McSteve Ezikeoha
        Title:   Binary Search Trees
        Date:    April 25, 2018
'''

# Problem 4.4: find_parent(self, some_node)
#       starting at the root, go down the BST until you find the node that is
#       the parent of some_node.
#       (non-recursive)

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
                if new_value < treeptr.payload:
                        if treeptr.left == None:
                                treeptr.left = BST.Node(new_value)
                        else:
                                BST.attach_in_order_aux(treeptr.left, new_value)
                elif new_value > treeptr.payload:
                        if treeptr.right == None:
                                treeptr.right = BST.Node(new_value)
                        else:
                                BST.attach_in_order_aux(treeptr.right, new_value)

        def isLeaf(some_node):
                if some_node.left == None and some_node.right == None:
                        return False
                else:
                        return True

        def getPath(self, some_node):
                pathList = []
                runner = self.root
                pathList.append(runner)
                while runner != None and runner != some_node:
                        if runner.payload > some_node.payload:
                                runner = runner.left
                                pathList.append(runner)
                        else:
                                runner = runner.right
                                pathList.append(runner)
                return pathList

        def find_parent(self, some_node):
                if self.root == some_node:
                        return None
                runner = self.root
                parent = self.root
                while runner != None and runner != some_node:
                        if runner.payload > some_node.payload:
                                parent = runner
                                runner = runner.left
                        else:
                                parent = runner
                                runner = runner.right
                return parent
        
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

	tree.attach_in_order("ape")
	tree.attach_in_order("elephant")
	tree.attach_in_order("yak")
	tree.attach_in_order("zorse")
	tree.attach_in_order("fly")
	tree.prettyprint()
	
	payload = "yak"
	parent = tree.find_parent(tree.find("yak"))
	print("The parent of ",payload,"is",parent.payload)

	parent = tree.find_parent(tree.find("zebra"))
	print("The parent of zebra is ",parent.payload)

	parent = tree.find_parent(tree.find("man"))
	if parent is None:
		print("Man has no parent")
	else:
		print("The parent of man is",parent.payload)
