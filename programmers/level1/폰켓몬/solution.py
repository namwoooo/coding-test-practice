import collections

def solution(nums):
    nums_type = collections.Counter(nums)  # 폰켓몬 종류별 count
    take_ct = len(nums) / 2 # 내가 가져갈 폰켓몬 수

    if take_ct <= len(nums_type):
        answer = take_ct
    else: 
        answer = len(list(nums_type.keys()))

    return answer