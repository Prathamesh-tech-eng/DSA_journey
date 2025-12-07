
'''
Problem Description : we are provided with an array, and an integer k. We need to find the the top k most frequently occuring elements among the given
                      array. 
                      e.g : [11,12,11,12,11,24]   k = 2, O/P: [11,12]

Problem Approach : we can just brute force it by iterating each element, taking their count, and then returning the k most frequent elements. To optimize
                   we can use Hash map to store the elements and it's frequency. this will significantly reduce the time complexity and then we can just 
                   sort the hash values and return the k values. We can further optimize it by using heap (priority queue) instead of sorting by defining 
                   array of only k size.
'''

# Hash Map + bucket Approach 

from collections import Counter

'''
def topKFrequent(nums ,k) :

    #Step 1 : Counting Frequencies
    freq_map = Counter(nums)  #same as using a dictionary : nums -> frequency

    #Step 2 : Createing buckets where index = frequency
    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in freq_map.items():
        buckets[freq].append(num)

    #Step 3 : Traversing buckets from highest frequency to lowest
    result = []
    for freq in range(len(buckets) - 1, -1, -1):
        if buckets[freq]:  #not empty
            result.extend(buckets[freq])  #add all numbers with this frequency

        if len(result) == k:
            return result[:k]
 '''       
    #Time Complexity : O(n)
    #Space Complexity : O(n)


# Sorted Hash map 
'''
def topKFrequent(nums ,k) :

    #Step 1 : Counting Frequencies
    freq_map = Counter(nums)  #same as using a dictionary : nums -> frequency

    #Step 2 : Sort items by frequency in descending order
    sorted_items = sorted(freq_map.items(), key = lambda x: x[1], reverse = True)

    #Step 3 : extract top k keys
    return [item[0] for item in sorted_items[:k]]
'''
    #Time Complexity : O(nlogn)
    #Space Complexity : O(n)

# Built in 
'''
def topKFrequent(nums, k):
    return [num for num, freq in Counter(nums).most_common(k)]
'''
    #Time Complexity : O(nlogn)
    #Space Complexity : O(n)


#Hash Map + Heapq
import heapq

def topKFrequent(nums ,k) :

    #Step 1 : Counting Frequencies
    freq_map = Counter(nums)  #same as using a dictionary : nums -> frequency

    #step 2 : Creating a min-heap
    min_heap = []

    #step 3 : Push items into heap, keeping size <= k
    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num)) #store (frequency, number)

        if len(min_heap) > k:
            heapq.heappop(min_heap) #remove smallest freq

        
    #Step 4 : Extract only numbers (Second Value in tuple)
    return [num for freq, num in min_heap]

    #Time Complexity : O(nlogk)
    #Space Complexity : O(n)
