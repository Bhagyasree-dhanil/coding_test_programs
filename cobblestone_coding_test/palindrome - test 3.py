""""

you are given a string S containing lowercase English letters. Your task is to calculate the minimum no of letters that
need to be removed inorder to make it possible to  build a palindrome from the remaining letters. when building the
palindrome ,you can arrange the remaining letters in any ways.

A palindrome is a string that reads the same both forwards and backwards.eg : radar,mom, kayak

Write a function
   def solution(S):
         your code here.

which, given a string of length N , returns the minimum no of letters that need to be removed.

Examples:

1. S = "ervervige" should return 2. After removing g , e we can create a palindrome "reviver"
2. S = "aaabab" should return 0 . "aabbaa" is  a palindrome
3. S = "x"  return 0 . x is palindrome

"""
"""

convert the string to set to remove duplicates and find the count of each element of set in the list. 
then  count the result with below conditions
if cnt is odd  (* if count is odd , it cannot form  a palindrome)
 or cnt = 1 ( * only take one element with count 1 .ignore count of others with count 1)


"""


def solution(S):
    conv_set = set(S)
    cnt = 0
    cnt_array = []
    for i in conv_set:
        val = S.count(i)
        if val % 2 != 0:
            cnt += 1
        cnt_array.append(val)

    if 1 in cnt_array:
        cnt -= 1

    print(cnt, conv_set, cnt_array)


inp1 = "aaabab"
inp2 = "ervervige"
inp3 = "x"
inp4 = "malayalam"
solution(inp1)
solution(inp2)
solution(inp3)
solution(inp4)