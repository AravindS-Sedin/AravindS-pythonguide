# BST Contact Book
#
# Real-world app:
# Phone contacts / address book
#
# Concepts:
# 1. Binary Search Tree (BST)
# 2. Iterative Insert
# 3. Iterative Search
# 4. Iterative Delete
# 5. Inorder Traversal (A-Z sorting)
# 6. Height Calculation
# 7. Balance Check
#
# Contacts are stored alphabetically using name as the key.


class ContactNode:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.left = None
        self.right = None


class ContactBook:

    def __init__(self):
        self.root = None

    # Insert a new contact
    def insert(self, name, phone, email):

        new_node = ContactNode(name, phone, email)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:

            if name < current.name:

                if current.left is None:
                    current.left = new_node
                    return

                current = current.left

            elif name > current.name:

                if current.right is None:
                    current.right = new_node
                    return

                current = current.right

            else:
                # Update existing contact
                current.phone = phone
                current.email = email
                return

    # Search contact by name
    def search(self, name):

        current = self.root

        while current:

            if name == current.name:
                return current

            elif name < current.name:
                current = current.left

            else:
                current = current.right

        return None

    # Delete contact by name
    def delete(self, name):

        parent = None
        current = self.root

        # Find node
        while current and current.name != name:

            parent = current

            if name < current.name:
                current = current.left
            else:
                current = current.right

        if current is None:
            print("Contact not found.")
            return

        # Case 3: Two children
        if current.left and current.right:

            successor_parent = current
            successor = current.right

            while successor.left:
                successor_parent = successor
                successor = successor.left

            current.name = successor.name
            current.phone = successor.phone
            current.email = successor.email

            parent = successor_parent
            current = successor

        # Case 1 & 2
        child = current.left if current.left else current.right

        # Deleting root node
        if parent is None:
            self.root = child

        elif parent.left == current:
            parent.left = child

        else:
            parent.right = child

        print(f"{name} deleted successfully.")

    # List all contacts in A-Z order
    def list_all(self):

        contacts = []
        stack = []
        current = self.root

        while stack or current:

            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            contacts.append(
                (current.name, current.phone, current.email)
            )

            current = current.right

        return contacts

    # Height of BST
    def height(self):

        if self.root is None:
            return 0

        queue = [self.root]
        height = 0

        while queue:

            level_size = len(queue)

            for _ in range(level_size):

                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            height += 1

        return height

    # Check if root is balanced
    def balance(self):

        if self.root is None:
            return True

        left_height = self.subtree_height(self.root.left)
        right_height = self.subtree_height(self.root.right)

        return abs(left_height - right_height) <= 1

    # Height of a subtree
    def subtree_height(self, root):

        if root is None:
            return 0

        queue = [root]
        height = 0

        while queue:

            level_size = len(queue)

            for _ in range(level_size):

                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            height += 1

        return height


def main():

    book = ContactBook()

    book.insert("John", "9876543210", "john@gmail.com")
    book.insert("Alice", "9123456789", "alice@gmail.com")
    book.insert("Mike", "9988776655", "mike@gmail.com")
    book.insert("Bob", "9000000000", "bob@gmail.com")
    book.insert("Kevin", "9555555555", "kevin@gmail.com")

    print("\nAll Contacts (A-Z)")
    for contact in book.list_all():
        print(contact)

    print("\nSearching for Mike")
    result = book.search("Mike")

    if result:
        print(
            result.name,
            result.phone,
            result.email
        )
    else:
        print("Contact not found")

    print("\nDeleting Alice")
    book.delete("Alice")

    print("\nContacts After Deletion")
    for contact in book.list_all():
        print(contact)

    print("\nBST Height:", book.height())
    print("Balanced:", book.balance())


if __name__ == "__main__":
    main()