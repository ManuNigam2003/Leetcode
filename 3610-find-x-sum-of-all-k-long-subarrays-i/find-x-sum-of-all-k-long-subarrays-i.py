class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        n = len(nums)

        if n < k:
            return [sum(nums)]
        
        hs = Counter()

        for i in range(k):
            hs[nums[i]] += 1
        
        j = 0
        arr = []

        sm = 0
        heap = []
        tmp = x
        for h in hs:
            heapq.heappush(heap, (-hs[h], -h))
        
        while heap and tmp != 0:
            value = heapq.heappop(heap)
            sm += (value[0] * value[1])
            tmp -= 1
        
        arr.append(sm)
    

        i += 1
        while i < len(nums):

            hs[nums[j]] -= 1
            hs[nums[i]] += 1
        
            i += 1
            j += 1

            sm = 0
            heap = []
            tmp = x
            for h in hs:
                heapq.heappush(heap, (-hs[h], -h))
            
            while heap and tmp != 0:
                value = heapq.heappop(heap)
                sm += (value[0] * value[1])
                tmp -= 1
            
            arr.append(sm)
        
        return (arr)
            
        