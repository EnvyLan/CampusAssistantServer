#coding=utf-8
__author__ = 'EnvyLan'
import  os

col = 0;row = 0;length=8
array=[]
def search(r):
	if (r == length):
		return

	array[col] = r
	ok = 1
	for j in enumerate(r):
		if((array[col] == array[j]) | (array[j]-array[col] == j-col) | (array[col]-array[j] == j-col)):
			ok = 0
			break
	if (ok == 1):
		search(r+1)

search(0)