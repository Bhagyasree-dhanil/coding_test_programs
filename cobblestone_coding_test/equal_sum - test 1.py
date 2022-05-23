"""
write  a function

def solution(A):
      your code here

given an array A of N integers, returns the maximum sum of two numbers whose digits add up to an equal sum.
if there are no two numbers whose digit have an equal sum , the function should return -1
examples:

1. Given A= [51, 71, 17,42] the function should return 93. There are two pairs of numbers whose digits add up to equal
sum (51,42) and (17,71). The first pair sum upto  93.

2. Given A = [42, 33, 60, 51] the function should return 102. the digits of all numbers in A add up to the same sum, and
choosing to add 42  and 60 gives result 102

3. Given A= [51,32,43] the function should return -1 ,since all numbers in A have digits that add up to different ,
unique forms


"""
"""
1. find sum of digits of elements in list
2. find elements with same sum
3. find sum of those 

"""


def digit_sum(n):
    num = 0
    for i in str(n):
        num = num + int(i)
    return num


def solution(A):
    mp = {}
    pairi = 0
    pairj = 0
    ans = -1
    for i in range(len(A)):

        val = digit_sum(A[i])
        if val not in mp:
            mp[val] = 0

        if mp[val] != 0:
            if mp[val] + A[i] > ans:
                pairi = A[i]
                pairj = mp[val]
                ans = pairi + pairj

        mp[val] = max(A[i], mp[val])
    print("MAP", pairi, pairj ,ans)


A = [51, 33, 60, 42]
print(solution(A))
