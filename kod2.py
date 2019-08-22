text = input("enter text: ").split()
a = []
for i in text:
	if not i in a:
		a.append(i)
b = ' '.join(a)
print(b)
	
