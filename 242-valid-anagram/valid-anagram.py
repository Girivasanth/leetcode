class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        dic_s={}
        dic_t={}
        for i in s:
            dic_s[i]=dic_s.get(i,0)+1
        for j in t:
            dic_t[j]=dic_t.get(j,0)+1
        s_val=list(dic_s.items())
        t_val=list(dic_t.items())
        if s_val==t_val:
            return True
        else:
            return False