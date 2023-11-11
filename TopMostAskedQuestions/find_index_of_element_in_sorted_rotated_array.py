"""
Write a program to find the index of a given element in array ‘A’ that is both sorted and rotated.
"""

def find_index_of_element_in_sorted_rotated_array(array, element):
  """Returns the index of the given element in the given sorted and rotated array, or None if the element is not in the array.

  Args:
    array: The sorted and rotated array to search.
    element: The element to search for.

  Returns:
    The index of the given element in the given sorted and rotated array, or None if the element is not in the array.
  """

  low = 0
  high = len(array) - 1

  while low <= high:
    mid = (low + high) // 2

    if array[mid] == element:
      return mid

    elif array[mid] >= array[low]:
      if array[low] <= element < array[mid]:
        high = mid - 1
      else:
        low = mid + 1

    else:
      if array[mid] < element <= array[high]:
        low = mid + 1
      else:
        high = mid - 1

  return None

# Example usage:

print(find_index_of_element_in_sorted_rotated_array([4, 5, 6, 7, 0, 1, 2, 3], 6))
