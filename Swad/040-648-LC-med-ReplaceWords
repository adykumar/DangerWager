"""
648. Replace Words
Medium

In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor.
For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:

Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Note:
The input will only have lower-case letters.
1 <= dict words number <= 1000
1 <= sentence words number <= 1000
1 <= root length <= 100
1 <= sentence words length <= 1000
"""

"""
Time- O(d)+O(s)- ie number of chars in dic + number of chars in sentence
Space- O(dl)- num of words in dic * avg word length. realistically lesser
"""

class Solution(object):

    def insertTrie(self, w, trie):
        temp= trie
        for ch in w:
            if ch not in temp: temp[ch]= {}
            temp= temp[ch]
        temp["end"]= None

    def replace(self, w, trie):
        temp= trie
        i=0
        for ch in w:
            if ch not in temp: break
            i+=1
            if "end" in temp[ch]:
                return True, w[:i]
            temp= temp[ch]
        return False, None

    def replaceWords(self, dict, sen):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie= {}
        for w in dict:
            self.insertTrie(w, trie)
        words= sen.split()
        res= []
        for word in words:
            a,b= self.replace(word, trie)
            if a:
                res.append(b)
            else:
                res.append(word)
        return ' '.join(res)
