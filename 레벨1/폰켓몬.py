#폰켓몬
def solution(nums):
    s = set()
    for i in nums:
        s.add(i)
    return min(len(s), len(nums)/2)