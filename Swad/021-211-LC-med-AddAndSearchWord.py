"""
211. Add and Search Word - Data structure design
Medium

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
"""

"""
Time- Add/Search- O(n)
Space- upperbound is w*l where:
    w= number of words inserted
    l= avg length of word
    the requirements reduce when more and more words have common prefixes
"""


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie= {"head":{}}


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        trav= self.trie["head"]
        for c in word:
            if c not in trav:
                trav[c]= {}
            trav= trav[c]
        trav[1]= {}


    def helper(self, trie, word):
        if word=="":
            if 1 in trie:
                return True
            else:
                return False
        res= False
        c= word[0]
        if c in trie :
            res= res or self.helper(trie[c], word[1:])
        elif c==".":
            for br in trie:
                res= res or self.helper(trie[br], word[1:])
        else:
            return False
        return res

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        trav= self.trie["head"]
        return self.helper(trav, word)




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
