class Node:
    def __init__(self, key):
        self.left = None
        self.data = key
        self.right = None
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.data == key:
            return root
        elif root.data < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
        return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)
def preorder(root):
    if root:
        print(root.data,end=' ')
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=' ')
def search(root,key):
    if root==None:
        print("key not found")
    elif root.data == key:
        print("Key found")
    elif root.data < key:
        return search(root.right,key)
    else:
        return search(root.left,key)
def min(root):
    temp = root
    while(temp.left is not None):
        temp = temp.left
    return temp.data
def max(root):
    temp = root
    while(temp.right is not None):
        temp = temp.right
    return temp.data
def height(root):
    if root is None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)
        max_height = lheight
        if rheight>max_height:
            max_height = rheight
        return max_height+1
def delete_Node(root, key):
    if not root:
        return root
    if root.data > key:
        root.left = delete_Node(root.left, key)
    elif root.data < key:
        root.right = delete_Node(root.right, key)
    else:
        if not root.right:
            return root.left
        if not root.left:
            return root.right
        temp_val = root.right
        mini_val = temp_val.data
        while temp_val.left:
            temp_val = temp_val.left
            mini_val = temp_val.data
        root.right = delete_Node(root.right,root.data)
    return root
b = Node(50)
b = insert(b, 30)
b = insert(b, 20)
b = insert(b, 40)
b = insert(b, 70)
b = insert(b, 60)
b = insert(b, 80)
print('inorder')
inorder(b)
print()
print('postorder')
postorder(b)
print()
print('preorder')
preorder(b)
print()
b = delete_Node(b,20)
print('after deleting 20')
preorder(b)
print()
print('Search')
search(b, 30)
print('Min')
print(min(b))
print('Max')
print(max(b))
print('height')
print(height(b))
