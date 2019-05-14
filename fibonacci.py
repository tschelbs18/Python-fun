# Fibonacci Sequence Function
# Simple Example of Recursion

def getnthfib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return getnthfib(n-1) + getnthfib(n-2)
