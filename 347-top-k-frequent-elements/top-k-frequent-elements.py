class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_count = defaultdict(int)

        for num in nums:
            num_count[num] += 1

        buckets = [[] for _ in range(max(num_count.values()))]

        for num,count in num_count.items():
            buckets[count-1].append(num)

        top_elements = []

        for index in range(len(buckets)-1,-1,-1):
            bucket = buckets[index]

            for num in bucket:
                if len(top_elements) == k:
                    return top_elements
                top_elements.append(num)

        return top_elements