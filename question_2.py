"""
Implement a function that reverses a string?
"""
def reverse(s):
  # start = 0
  # end = len(s)-1
  # while start <= end:
  #   temp = s[start]
  #   s.replace(s[start],s[end])
  #   #s.replace(s[end],temp)
  #   end -= 1
  #   start += 1
  # return s
  return "".join(reversed(list(s)))
  # O(n) time
  # O(n) Space or O(1) maybe

print(reverse("abcd"))