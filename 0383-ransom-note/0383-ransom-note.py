class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map = dict()
        max_len = max(len(ransomNote), len(magazine))

        for i in range(max_len):
            if i < len(ransomNote):
                hash_map[ransomNote[i]] = hash_map.get(ransomNote[i], 0) - 1
            
            
            if i < len(magazine):
                hash_map[magazine[i]] = hash_map.get(magazine[i], 0) + 1

        
        return len([val for val in hash_map.values() if val < 0]) == 0