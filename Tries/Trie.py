# Author: mspagon
# Date: 5/12/18 4:40 PM

# Problem: https://www.hackerrank.com/challenges/ctci-contacts/problem


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

            child_position = current_node.search(letter)  # search children of current_node for letter

            if child_position != -1:  # letter found!
                current_node = current_node.children[child_position]
                current_node.increment_count()
            else:
                new_node = Node(letter)
                current_node.children.append(new_node)
                current_node = new_node

    def find(self, name: str) -> int:
        """count how many times 'name' appears in the Trie

        In other words, count how many leaf nodes are within the subtree specified by 'name'.
        """
        current_node = self.head

        for i, letter in enumerate(name):

            child_position = current_node.search(letter)  # search children of current_node for letter

            if child_position != -1:  # if letter was found advance current_node
                current_node = current_node.children[child_position]

                if i == len(name) - 1:  # if this was last letter in word, return count.
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
