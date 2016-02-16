
list = [1,2]
even_list2 = []

def pop_first(i):
	return list[-1]

def pop_second(i):
	return list[-2]
	
while list[-1] < 4000000 :
	x = list[-1] + list[-2]
	list.append(x)

for i in list:
	if i % 2 == 0:
		even_list2.append(i)

	
print pop_first(list)
print pop_second(list)
print list
print even_list2
print sum(even_list2)