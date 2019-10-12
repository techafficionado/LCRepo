def concatenatedWords(allwords):

    def recWord(word):
        for i in range(1,len(word)):
                if (word[:i] in words)  and (word[i:] in words or recWord(word[i:])):
                    return True
        return False


    minlen = 0
    words = set()
    for word in allwords:
        minlen = min(minlen,len(word))
        words.add(word)

    concatwords = [] 
    for word in words:
        if len(word) == minlen:
            continue
        for i in range(1,len(word)):
                 if (word[:i] in words and (word[i:] in words or recWord(word[i:]))):
                    concatwords.append(word)
                    break
    print("concatwords:{}".format(concatwords))
    return concatwords












words=["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
words=["g","f","v","e","gfve"]
print(concatenatedWords(words))
