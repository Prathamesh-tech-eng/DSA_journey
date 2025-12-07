'''
    Problelm Description : I am provided with an array, and i need to return an answer array where each index element has a value that is product of 
                           all other index values except itself. The solution strictly needs to be of O(n) time complexity. The use of division approach
                           is restricted.

                           e.g : [10, 20, 30, 40]   O/P : [24000, 12000, 8000, 6000]


    Problem Approach : Brute force mgiht have worked, where we would use two for loops and just find product for each index seperately, but it will cost
                       O(N2) time complexity. so we are avoiding that. Next is prefix and suffix approach. we will have pre consisting of product value of 
                       before target index and pro consisting of product of after index values. so each time we won't need to iterate to find the product. We 
                       can optimize it further by just creating a single array ans instead of creating seperate arrays for pre, post and ans
                       
'''


#Using two arrays that is prefix and postfix
'''
def productExceptSelf(nums):
    n = len(nums)
    result = [0] * n
    pre = [1] * n
    post = [1] * n

    # prefix product
    for i in range(1, n):
        pre[i] = nums[i-1] * pre[i-1]

    # suffix product
    for j in range(n-2, -1, -1):
        post[j] = nums[j+1] * post[j+1]

    # result = prefix * suffix
    for k in range(n):
        result[k] = pre[k] * post[k]

    return result

'''
#Time Complexity : O(3n) ~ O(n)
#Space Complexity : O(n)

#Optimal Solution
def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n

    # prefix pass
    prefix = 1
    for i in range(n):
        result[i] = prefix 
        prefix *= nums[i]
        

    # suffix pass
    postfix = 1
    for j in range(n-1, -1, -1):
        result[j] *= postfix
        postfix *= nums[j]

    return result

#Time Complexity : O(2n) ~ O(n)
#Space Complexity : O(1)
