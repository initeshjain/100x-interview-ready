"""
Write a program to convert a long URL to a short URL leading to the same web page.

There are a number of ways to convert a long URL to a short URL. One common approach is to use a base62 encoding scheme. The following Python code shows how to do this:
"""

import base62

def convert_long_url_to_short_url(long_url):
  """Converts a long URL to a short URL using base62 encoding.

  Args:
    long_url: The long URL to convert.

  Returns:
    A short URL leading to the same web page as the long URL.
  """

  short_url = base62.encode(long_url)

  return short_url


long_url = "https://www.noobgeek.in/blogs/what-is-useragents-all-about-useragents-in-respect-to-web-development-and-browser"
print(convert_long_url_to_short_url(long_url))