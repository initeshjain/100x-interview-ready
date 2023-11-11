"""
Write a code to convert a given set of integers into their Roman number equivalents.
"""

def int_to_roman(num):
  """Converts an integer to a Roman numeral.

  Args:
    num: The integer to convert.

  Returns:
    A string representing the Roman numeral equivalent of the given integer.
  """

  roman_numerals = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M",
  }

  roman_numeral = ""
  for value in sorted(roman_numerals.keys(), reverse=True):
    while num >= value:
      roman_numeral += roman_numerals[value]
      num -= value

  return roman_numeral

# Example usage:

print(int_to_roman(1234))
