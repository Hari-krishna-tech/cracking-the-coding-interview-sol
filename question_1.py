"""
Implement an algorithm to determine if a string has all unique characters.What if you cannot use additional data structure?
"""
def allUnique(s):
  # # Brute force
  # for idx,val in enumerate(s):
  #   if val in s[idx+1:]:
  #     return False
  # return True
  # O(n^2) time 
  # O(1) space 

  # n = len(s)
  # if n > 256 :
  #   return False
  # contains = [False]*256
  # for i in s:
  #   if contains[ord(i)]:
  #     return False
  #   contains[ord(i)] = True
  # return True
  #time O(n)
  #space O(1) constant


  
print(allUnique("abcdeff"))
