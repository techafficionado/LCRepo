class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        ALGORITHM
        FOR EACH STR IN STRS BUILD CHAR LIST COUNT AND ADD IT TO HMAP AS A TUPLE.
        RETURN ALL HMAP VALUES
        '''
        hmap = collections.defaultdict(list)
        for str1 in strs:
            chars = [0]*26
            for char in str1:
            
                chars[ord(char)-ord('a')] += 1
            hmap[tuple(chars)].append(str1)
            
        return list(hmap.values())
        
        
