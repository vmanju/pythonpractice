#!/usr/bin/python
#This Python file uses the following encoding: utf-8

"""
Exercise 6.5 Take the following Python code that stores a string:‘
str = ’X-DSPAM-Confidence: 0.8475’
Use find and string slicing to extract the portion of the string after the colon character and then
use the float function to convert the extracted string into a ﬂoating point number.
"""

string = "X-DSPAM-Confidence: 0.8475"
start_index = string.find(':')
num = string[start_index+1:].strip()
print float(num)


