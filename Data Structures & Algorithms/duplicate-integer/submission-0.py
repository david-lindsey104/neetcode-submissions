class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_list = {}
        for i in nums:
            if dict_list.get(i) == None:
                dict_list[i] = 1
            else:
                dict_list[i] += 1

            if dict_list.get(i) > 1:
                return True

        return False