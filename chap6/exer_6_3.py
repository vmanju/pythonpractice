#!/usr/bin/python
#This Python file uses the following encoding: utf-8

def count(fruit, character):
	frequency = 0
	for letter in fruit:
		print letter
		if letter == character:
			frequency+=1
	return frequency

print count('banana', 'a')
