class Node:
    def __init__(self):
        self.children=[None]*26
        self.isTreminal=False

class Trie:
    def __init__(self):
        self.root=Node()

    def charIndex(self,ch):
        return ord(ch)-ord("a")

    def insert(self,new_word):
        curr=self.root
        for level in range(len(new_word)):
            i=self.charIndex(new_word[level])

            if curr.children[i]==None:
                curr.children[i]=Node()
            curr =curr.children[i]

        curr.isTreminal=True

    def search(self,key):
        curr=self.root
        for level in range(len(key)):
            i=self.charIndex(key[level])

            if curr.children[i]==None:
                return False
            curr=curr.children[i]


        return curr.isTreminal

    def check_prefix(self,key):
            curr=self.root
            for level in range(len(key)):
                i=self.charIndex(key[level])

                if curr.children[i]==None:
                    return False
                curr=curr.children[i]


            return True
    def isChildren(self,root):
        for i in range(len(root.children)):
            if root.children[i]:
                return True
        return False

    def delete(self,key,root):

        i=self.charIndex(key[0])
        if root.children[i]==None:
            #if word is not found
            return False



        if len(key)>1:
            # recursively calling function by removing first character of key and going downward in trie
            to_remove=self.delete(key[1:], root.children[i])
            # to_remove is flag showing to check if we can remove any node

        else:
            root.children[i].isTreminal=False
            to_remove=True
            # at last we have to check if we can remove
        if to_remove:
            # TO REMOVE SAYS THERE IS POSSIBILITY TO REMOVE CHARACTER


            if self.isChildren(root.children[i]):
                # if there is child of node we cant remove character
                return False
            else:
                root.children[i]==None
                return True

        return False


















t=Trie()
t.insert("bcde")
t.insert("bcdef")
print(t.search("bcde"))
print(t.search("bcde"))
print(t.delete("bcde",t.root))
print(t.search("bcde"))
print(t.search("bcdef"))

