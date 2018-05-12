# Author: mspagon
# Date: 5/12/18 4:40 PM


class Node:
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.count = 1  # Initial count is 1

    def search(self, char: str) -> int:
        """Search for char amongst children nodes and return position if found"""
        for i, child in enumerate(self.children):
            if child.char == char:
                return i
        return -1

    def increment_count(self):
        self.count += 1


class Trie:
    def __init__(self):
        self.head = Node('0')  # 0 is the head value

    def add(self, name: str):
        """Add a string to the Trie"""
        current_node = self.head

        for i, letter in enumerate(name):  # for each letter in name

            char_found = 0

            for child in current_node.children:  # for each child

                if letter == child.char:
                    child.increment_count()
                    current_node = child
                    char_found = 1
                    break

            if char_found == 0:
                new_node = Node(letter)
                current_node.children.append(new_node)
                current_node = new_node

    def find(self, name: str) -> int:
        current_node = self.head

        for i, letter in enumerate(name):

            child_position = current_node.search(letter)

            if child_position != -1:
                current_node = current_node.children[child_position]

                if i == len(name) - 1:
                    return current_node.count
            else:
                return 0


def main():
    my_trie = Trie()

    f = open("input.txt", "r")
    line = f.readline()  # discard first line
    line = f.readline()

    while line:
        op, contact = line.strip('\n').split(' ')

        if op == 'add':
            my_trie.add(contact)
        if op == 'find':
            print(my_trie.find(contact))

        line = f.readline()


if __name__ == "__main__":
    main()
