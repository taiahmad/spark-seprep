class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            if len(strs[0]) <= i:
                return prefix

            for j in range(1, len(strs)):
                if len(strs[j]) <= i:
                    return prefix
                if strs[j][i] != strs[j - 1][i]:
                    return prefix

            prefix += strs[0][i]

        return prefix