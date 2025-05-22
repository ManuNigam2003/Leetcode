class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        q = deque(sorted(queries))
        c=0
        sub=[0 for _ in range(len(nums)+1)]
        countOfQueriesUsed = 0
        heap=[]
        for i in range(len(nums)):
            c-=sub[i]
            while q and q[0][0]==i:
                heapq.heappush(heap,-q.popleft()[1])
            while nums[i]>c:
                #we will have to use heap
                if not heap:
                    return -1
                last = -heapq.heappop(heap)
                if last<i:
                    continue
                else:
                    c+=1
                    sub[last+1]+=1
                    countOfQueriesUsed+=1
        #queries not used will be in heap
        return len(queries)-countOfQueriesUsed



                    