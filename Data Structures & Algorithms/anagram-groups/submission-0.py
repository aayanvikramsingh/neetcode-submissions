class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        for i in range(len(strs)):
            count[i] = {}
            for ch in strs[i]:
                count[i][ch] = count[i].get(ch, 0) + 1
        ans = []
        visited = set()
        for i in range(len(count)):
            if i in visited:
                continue
            ans.append([strs[i]])
            for j in range(i + 1, len(count)):
                if count[i] == count[j]:
                    ans[len(ans) - 1].append(strs[j])
                    visited.add(j)

        return ans
