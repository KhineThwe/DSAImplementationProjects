"""Implementation of Binary search tree algorithm with python min console project"""
class Node:
    """Instead of key,we insert name and pwd as a key"""
    def __init__(self,name,pwd):
        self.name=name
        self.pwd=pwd
        self.left=None
        self.right=None

def insert(node,name,pwd):
    """If node is none we need to return Node type"""
    if node is None:
        return Node(name,pwd)

    newName,totalValue1=aciiValue(name)
    oldName,totalValue=aciiValue(node.name)

    """Duplicate names are not allowed here"""
    if totalValue1==totalValue:
        print("Same name not allowed Here")
        return node

    for i in range(len(newName)):
        if newName[i] < oldName[i]:
            node.left = insert(node.left, name, pwd)
            break
        elif newName[i] > oldName[i]:
            node.right = insert(node.right, name, pwd)
            break

    return  node

"""Evaluatin ASCII value of name"""
def aciiValue(name):
    asciiList=[]
    totalValue=0
    """Firstly we convert all name into lower case"""
    lowerName=name.lower()
    for i in lowerName:
        acValue = ord(i)
        asciiList.append(acValue)
        totalValue=totalValue+ord(i)
    asciiList.append(1)

    return asciiList,totalValue

"""To print inorder------>left root right"""
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.name)
        inorder(root.right)

def login(root,name,pwd):
    if root is not None:
        if root.name == name and root.pwd == pwd:
            print("Login Successful!!")
            return
        else:
            login(root.left,name,pwd)
            login(root.right,name,pwd)

def search(root,name):
    if root is not None:
        if root.name == name:
            print("We found data")
            return
        else:
            search(root.left,name)
            search(root.right, name)

if __name__ == "__main__":
    root=None
    while True:
        option = int(input("Press 1 to register\n Press 2 to login\n\nPress 3 to search\n\n"))
        if option == 1:
            name = input("enter name to register>:")
            pwd = input("insert pwd to register>:")
            root = insert(root, name, pwd)
            inorder(root)
        elif option == 2:
            print("~~~~~~This is from login route~~~~~")
            name = input("enter name to login>:")
            pwd = input("insert pwd to login>:")
            login(root,name,pwd)
        else:
            name = input("enter name to search>:")
            search(root, name)
