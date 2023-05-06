from binarytree import build, Node

# Construct a binary tree from a list of integers
data = [4, 2, 1, 3, 6, 5, 7]
root = build(data)

# Print the binary tree
print("Binary Tree:")
print(root)

while True:
    # Ask the user for their choice
    print("Enter 1 to add an element, 2 to delete an element, or 0 to exit:")
    choice = int(input())

    if choice == 0:
        # Exit the program
        break
    elif choice == 1:
        # Add a new element to the binary tree
        value = int(input("Enter the value of the new element to add: "))
        new_node = Node(value)
        root.insert(new_node)
        print("New element added to the binary tree:")
        print(root)
    elif choice == 2:
        # Delete an element from the binary tree
        value = int(input("Enter the value of the element to delete: "))
        node_to_delete = root.search(value)
        if node_to_delete is None:
            print("Element not found in the binary tree!")
        else:
            root.delete(node_to_delete)
            print("Element deleted from the binary tree:")
            print(root)
    else:
        print("Invalid choice! Please enter 1, 2, or 0.")
