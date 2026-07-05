class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        buckets = {}
        lenWord = len(beginWord)
        wordToPattern = {}

        def createBuckets(word):
            return [word[:i] + "*" + word[i+1:] for i in range(lenWord)]

            toRet = []
            wordToAdd = list(word)
            for i in range(lenWord):
                temp = wordToAdd.copy()
                temp[i] = "*"
                temp = srt(temp)
                toRet.append(temp)
            return toRet

        check = False
        wordList.append(beginWord)
        for word in wordList:
            if endWord == word:
                check = True
            bucketList = createBuckets(word)
            wordToPattern[word] = bucketList
            for bucket in bucketList:
                if bucket not in buckets:
                    buckets[bucket] = [word]
                else:
                    buckets[bucket].append(word)
        if check is False:
            return 0
        
        visiting = set()
        visiting.add(beginWord)
        q = deque([(beginWord, 0)])

        while q:
            word, steps = q.pop()
            if word == endWord:
                return steps+1
            for pattern in wordToPattern[word]:
                neighbors = buckets[pattern]
                for nei in neighbors:
                    if nei not in visiting:
                        visiting.add(nei)
                        q.append((nei, steps+1))
                buckets[pattern] = []
        return 0




