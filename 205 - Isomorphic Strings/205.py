class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        
        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if (c1 not in map_s and c2 not in map_t):
                map_s[c1] = c2
                map_t[c2] = c1
            elif map_s.get(c1) != c2 or map_t.get(c2) != c1:
                return False

        return True 