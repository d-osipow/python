
x = list(map(int,input('Введите числа через пробел ').split()))
def function(x):
	x.sort(reverse=True)
	print('наибольшее число', x[0])
	print('его длинна', len(str(x[0])))
	print('наименьшее число ', x[-1])
	print('его длинна', len(str(x[-1])))
function(x)