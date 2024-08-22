from collections import Counter
from heapq import *

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Make a dictionary of counts
        freq_dict = Counter(words)
        
        # Find max frequency
        max_freq = max(freq_dict.values())
        
        # Make Max frequency + 1 buckets
        buckets = [[] for _ in range(max_freq + 1)]

        # Heap push word/key in bucket corresponding to freq
        for key, val in freq_dict.items():
            heappush(buckets[val], key)
        
        ans = []
        bucket_index = max_freq
        while k > 0 :
            if len(buckets[bucket_index]) > 0:
                ans.append(heappop(buckets[bucket_index]))
                k -= 1
            else:
                bucket_index -= 1
            
        return ans