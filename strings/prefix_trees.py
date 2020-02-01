from typing import List


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, w: str) -> None:
        """
        from root, check if there is a sub-tree for each character in the given word
        :param w: word to be added
        :return: none
        """
        current_node = self.root
        for c in w:
            if c in current_node.children:
                print("{} is already available as a child".format(c))
            else:
                print("creating a new child for {}".format(c))
                current_node.children[c] = TrieNode()
            current_node = current_node.children[c]
        current_node.is_end_of_word = True

    def find_word(self, word: str) -> bool:
        if not word:
            return False
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                return False  # did not find any path further
            print("found {} as a child".format(c))
            current_node = current_node.children[c]
        return current_node.is_end_of_word

    def get_all_words_matching_a_prefix(self, prefix: str) -> List:
        if not prefix:
            return []
        current_node = self.root
        path = list()
        output = list()
        for c in prefix:
            if c not in current_node.children:
                return []
            path.append(c)
            current_node = current_node.children[c]
        self.__collect_all_words_from_a_node(current_node, path, output)
        return output

    def __collect_all_words_from_a_node(self, node, path, output) -> List:
        if node.is_end_of_word:
            output.append("".join(path))
        for k, v in node.children.items():
            path.append(k)
            self.__collect_all_words_from_a_node(v, path, output)
            path.pop()  # restoring path before going to another path
        return output


sample_trie = Trie()
sample_trie.add("avi")
sample_trie.add("a")
sample_trie.add("arvind")
sample_trie.add("avinash")
sample_trie.add("aviarv")
print(sample_trie.find_word("rocky"))
print(sample_trie.find_word("avi"))
print(sample_trie.find_word("avin"))
print(sample_trie.find_word("arvind"))

print(sample_trie)

print("Printing all words matching a prefix: {}".format(sample_trie.get_all_words_matching_a_prefix("avi")))

a = {1: "abc", 2: "def"}
print(a)
print(a[1])
a[3] = "xyz"
print(a[3])
a[1] = "pqr"
print(a[1])
print(a)
print(10 in a)
for key, value in a.items():
    print("key: {}, value:{}".format(key, value))
for index, key1 in enumerate(a):
    print("key: {}, value:{}".format(index, key1))
