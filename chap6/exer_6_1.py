#!/usr/bin/python
# This Python file uses the following encoding: utf-8

"""
Exercise 6.1 Write a while loop that starts at the last character in the string and works its way backwards to the ﬁrst character in the string, printing each letter on a separate line, except backwards.
"""

fruit = "banana"
index = len(fruit) - 1
while index >= 0:
	print fruit[index]
	index-=1




