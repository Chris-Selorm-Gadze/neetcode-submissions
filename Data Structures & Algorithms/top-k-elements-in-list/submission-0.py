class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import defaultdict
        import heapq 

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        top_k = heapq.nlargest(k, freq, key = freq.get)

        return top_k