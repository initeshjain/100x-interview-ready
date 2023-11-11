"""
Divide an array consisting of integer elements into two sets such that the difference between the sum of both sets is an absolute minimum.
"""

def partition_array_with_minimum_sum_difference(array):
  """Divides the given array into two sets such that the difference between the sum of both sets is an absolute minimum.

  Args:
    array: The array to divide.

  Returns:
    A list of two lists, where each sublist represents one of the two sets.
  """

  total_sum = sum(array)
  target_sum = total_sum // 2

  dp = [[0] * (target_sum + 1) for _ in range(len(array) + 1)]

  for i in range(1, len(array) + 1):
    for j in range(1, target_sum + 1):
      if array[i - 1] <= j:
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - array[i - 1]] + array[i - 1])
      else:
        dp[i][j] = dp[i - 1][j]

  if dp[-1][-1] != target_sum:
    return None

  # Reconstruct the two sets.

  set1 = []
  set2 = []

  i = len(array)
  j = target_sum

  while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
      set2.append(array[i - 1])
      i -= 1
    else:
      set1.append(array[i - 1])
      j -= array[i - 1]
      i -= 1

  return [set1, set2]

# Example usage:

print(partition_array_with_minimum_sum_difference([1, 2, 3, 4, 5, 6, 7]))
