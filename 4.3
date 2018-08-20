'''
        Author:  McSteve Ezikeoha
        Title:   Binary Search Trees
        Date:    April 25, 2018
'''

# Problem 4.3: getPath(self, some_node)
#       starting at the root, form a list of node pointer down to the node.
#       We can use a list comprehension then to get the payloads if we want.
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
                if self.root == None:
                        return
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
	
	x = tree.find("yak")
	print("The path to yak is ",end="")
	print([y.payload for y in tree.getPath(x)])
