class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        e=enumerate
        return next(([i,j]for i,x in e(n)for j,y in e(n)if x+y==t and i!=j),)