"""
Write a program to find out if a given number “N” is sparse. (A number is said to be sparse if no two bits are in binary representation).
"""

def is_sparse(num):
  """Returns True if the given number is sparse, False otherwise.

  A number is said to be sparse if no two bits are set in its binary representation.

  Args:
    num: The number to check.

  Returns:
    True if the given number is sparse, False otherwise.
  """

  binary_representation = bin(num)[2:]
  for i in range(len(binary_representation) - 1):
    if binary_representation[i] == "1" and binary_representation[i + 1] == "1":
      return False

  return True

# Example usage:

print(is_sparse(10))
