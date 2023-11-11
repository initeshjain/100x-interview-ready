"""
Find the length of the longest increasing subsequence from a given array of n integers.
"""

def longest_increasing_subsequence(array):
  """Returns the length of the longest increasing subsequence in the given array.

  Args:
    array: The array to search.

  Returns:
    The length of the longest increasing subsequence in the given array.
  """

  dp = [1] * len(array)

  for i in range(len(array)):
    for j in range(i):
      if array[i] > array[j] and dp[i] < dp[j] + 1:
        dp[i] = dp[j] + 1

  return max(dp)

# Example usage:

print(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 44, 66, 33]))
