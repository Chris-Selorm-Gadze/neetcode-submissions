'''
sort. 

hashMap = {} {value : list}
 



'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)

        for s in strs: # ["act","pots","tops","cat","stop","hat"]
            count = [0] * 26  # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                              # [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
            
            for c in s: # pots
                count[ord(c) - ord('a')] += 1 

            result[tuple(count)].append(s) # {([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                                                   # : [act] }
        
        return list(result.values())  
