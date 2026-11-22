class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        right_max = - 1
        ans = [0] * length
        for i in range(length - 1, -1, -1):
            ans[i] = right_max
            right_max = max(arr[i], right_max)
        return ans

            


