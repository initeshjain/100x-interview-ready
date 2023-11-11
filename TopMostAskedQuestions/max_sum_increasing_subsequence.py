"""
Write a program to find the maximum sum increasing subsequence of a given array arr[].
"""

def max_sum_increasing_subsequence(array):
  """Returns the maximum sum of an increasing subsequence in the given array.

  Args:
    array: The array to search.

  Returns:
    The maximum sum of an increasing subsequence in the given array.
  """

  dp = [array[0]] * len(array)

  for i in range(1, len(array)):
    for j in range(i):
      if array[i] > array[j] and dp[i] < dp[j] + array[i]:
        dp[i] = dp[j] + array[i]

  return max(dp)

# Example usage:

print(max_sum_increasing_subsequence([10, 22, 9, 33, 21, 50, 44, 66, 33]))

