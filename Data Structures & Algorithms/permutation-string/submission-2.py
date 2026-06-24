class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #checking if s2 is smaller than s1, in that case s1 can't be permutation of s2
        if len(s1) > len(s2):
            return False

        countS1 = defaultdict(int)
        for i in range(len(s1)):
            countS1[s1[i]] += 1
        l = 0
        for r in range(len(s1) - 1, len(s2)):
            countS2 = defaultdict(int)
            for j in range(l, r + 1):
                countS2[s2[j]] += 1
            if countS1 == countS2:
                return True
            l += 1
        return False
