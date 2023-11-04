class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        res = len(list1)+len(list2)
        ans = {}
        x = []
        for word in list1:
            if word == " ":
                continue
            if word in list2:
                ln = list1.index(word)+list2.index(word)
                res = min(res,ln)
                ans[word]=ln
        
        for key, val in ans.items():
            if val==res:
                x.append(key)
                
        return x