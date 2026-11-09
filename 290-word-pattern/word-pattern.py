class Solution(object):
    def wordPattern(self, pattern, s):
        s=s.split(" ")
        p_len=len(pattern)
        if p_len!=len(s):
            return False
        dic={}
        dic2={}
        for i in range(p_len):
            if pattern[i] in dic:
                if dic[pattern[i]]!=s[i]:
                    return False
            if s[i] in dic2:
                if dic2[s[i]]!=pattern[i]:
                    return False
            dic[pattern[i]]=s[i]
            dic2[s[i]]=pattern[i]
        return True
        