class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #check to make sure same length
        if len(s) != len(s): return False

        sort_s = "".join(sorted(s))
        sort_t = "".join(sorted(t))

        if sort_s == sort_t: return True

        return False

        