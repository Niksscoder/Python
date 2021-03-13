def fib(n):
	a = 0
	b = 1
	for i in range(n):
		yield a
		a, b = b, a+b

num = int(input())
data = fib(num)
print(*data)