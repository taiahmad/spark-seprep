def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxe = []
        idx = 1
        for i in s:
            string = []
            st = set()
            st.add(i)
            string.append(i)
            for j in s[idx:len(s)]:
                if j not in st:
                    st.add(j)
                    string.append(j)
                elif j in st:
                    break
                else: print('AH!')
            if len(string) >= len(maxe):
                    maxe = string

            idx+=1
        return len(maxe)

