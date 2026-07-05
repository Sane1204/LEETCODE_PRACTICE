class Solution:
    ##submitting previous leetcode
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        for ele in strs:
            key = "".join(sorted(ele))
            if key not in map:
                map[key]=[]
            map[key].append(ele)
        ans=[]
        for key in map:
            ans.append(map[key])

        return ans

