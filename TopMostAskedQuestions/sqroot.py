"""
Write a code to compute the square root of a given number.

There are a number of ways to compute the square root of a given number. One simple method is to use the binary search algorithm. The following Python code shows how to do this:
"""

def binary_search_square_root(n):
  """Computes the square root of a given number using binary search.

  Args:
    n: The number to compute the square root of.

  Returns:
    The square root of n, or None if n is negative.
  """

  if n < 0:
    return None

  low = 1
  high = n

  while low <= high:
    mid = (low + high) // 2
    mid_squared = mid * mid

    if mid_squared == n:
      return mid
    elif mid_squared < n:
      low = mid + 1
    else:
      high = mid - 1

  return None

# Example usage:

square_root = binary_search_square_root(int(input("write a number -> ")))
print(square_root)
