class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

       
   
        obj = {}
        obj2 = {}

        for i in range(len(ransomNote)):
            if ransomNote[i] not in obj:
                obj[ransomNote[i]] = 0
            else:
                obj[ransomNote[i]] += 1
            
        for j in range(len(magazine)):
            if magazine[j] not in obj2:
                obj2[magazine[j]] = 0
            else:
                obj2[magazine[j]] += 1

        
        for x in obj:
            if x in obj and x in obj2:
                if obj.get(x) > obj2.get(x):
                    return False
            else:
                return False

        return True
            
        