"""
Given  an  array consisting of N integers, returns the biggest value X, which occurs in A exactly x times. If there is
no such values, the function should return 0

given A= [3,8,2,3,3,2] the function should return 3. The value 2 occurs exactly two times and value 3 occurs exactly
three times, so both meet task condition. THe value 8 occurs just once , thus it doesnot meet the task conditions. The
maximum of 2 and 3 is 3.

given A =[7,1,2,8,2] the function should return 2. The value 1 occur exactly one time, the value 2 occur exactly two time

given A = [3,1,4,1,5] , the function should return 0. no value which meet the condition.

"""


def solution(A):
    count_arr =[]
    for i in set(A):
        cnt = A.count(i)
        if cnt == i:
            count_arr.append(cnt)
    print(count_arr)

    if len(count_arr) == 0:
        return 0
    return max(count_arr)


A= [7,1,2,8,2]
print(solution(A))