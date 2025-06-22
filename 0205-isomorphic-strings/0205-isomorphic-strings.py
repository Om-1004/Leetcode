class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        hash_map = {}

        for i in range(len(s)):

            if s[i] not in hash_map.keys():
                if t[i] in hash_map.values():
                    return False
                else:
                    hash_map[s[i]] = t[i]
            else:
                val = hash_map[s[i]]
                if val != t[i]:
                    return False
        return True  

