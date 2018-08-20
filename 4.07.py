'''
        Author:  McSteve Ezikeoha
        Title:   Binary Search Trees
        Date:    May 6, 2018
'''

# Problem 4.7: traverse(some_node, "inorder")
#       traverse the tree whose root is some_node in "inorder", "preorder" or "postorder".
#       (recursive)
#       This returns a list of nodes.

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
        
        def isBST(some_node):
                if some_node.left == None and some_node.right == None:
                        return True
                if some_node.left != None:
                        if some_node.left.payload > some_node.payload:
                                return False
                        else:
                                return BST.isBST(some_node.left)
                if some_node.right != None:
                        if some_node.right.payload < some_node.payload:
                                return False
                        else:
                                return BST.isBST(some_node.right)
                else:
                        return True
                
        def flip(self):
                BST.flip_aux(self.root)

        def flip_aux(some_node):
                runner = some_node
                temp = some_node
                if runner == None:
                        return None
                if runner.left != None or runner.right != None:
                        temp = runner.left
                        runner.left = runner.right
                        runner.right = temp
                        return BST.flip_aux(some_node.left), BST.flip_aux(some_node.right)
                
        def traverse(some_node, order):
                nodes = []
                if order == "preorder":
                        def _traverse_pre_order_aux(some_node):
                                if not some_node:
                                        return
                                nodes.append(some_node)
                                if some_node.left != None:
                                        _traverse_pre_order_aux(some_node.left)
                                if some_node.right != None:
                                        _traverse_pre_order_aux(some_node.right)
                        _traverse_pre_order_aux(some_node)
                        return nodes
                
                elif order == "inorder":
                        def _traverse_in_order_aux(some_node):
                                if not some_node:
                                        return
                                if some_node.left != None:
                                        _traverse_in_order_aux(some_node.left)
                                nodes.append(some_node)
                                if some_node.right != None:
                                        _traverse_in_order_aux(some_node.right)
                        _traverse_in_order_aux(some_node)
                        return nodes
                
                elif order == "postorder":
                        def _traverse_post_order_aux(some_node):
                                if not some_node:
                                        return
                                if some_node.left != None:
                                        _traverse_post_order_aux(some_node.left)
                                if some_node.right != None:
                                        _traverse_post_order_aux(some_node.right)
                                nodes.append(some_node)
                        _traverse_post_order_aux(some_node)
                        return nodes
                else:
                        print("traverse the tree whose root is some_node in 'inorder'",
                                "'preorder' or 'postorder'")
                
        
                                             
if __name__ == "__main__":
	tree = BST()
	tree.root = BST.Node("man")
	tree.attach_in_order("dog")
	tree.attach_in_order("zebra")
	tree.attach_in_order("ape")
	tree.attach_in_order("elephant")
	tree.attach_in_order("yak")
	tree.attach_in_order("zorse")
	tree.attach_in_order("fly")
	tree.prettyprint()

	traversed = BST.traverse(tree.root, "preorder")
	#print(traversed)
	print([x.payload for x in traversed])

	traversed = BST.traverse(tree.root, "inorder")
	print([x.payload for x in traversed])

	traversed = BST.traverse(tree.root, "postorder")
	print([x.payload for x in traversed])
