def nod(firstnumber, secondnumber) -> int:
	if type(firstnumber) != type(1) or type(secondnumber) != type(1):
		return('Введите целое число')
		# если ввели не целое число, то возвращаем вышенаписанную строку

	if firstnumber == 0:
		return(secondnumber)
	elif secondnumber == 0:
		return(firstnumber)
		# если одно из чисел равно нулю, то возвращаем наибольшее число

	while secondnumber != 0:
		firstnumber, secondnumber = secondnumber, firstnumber % secondnumber
		# цикл находит нод
	return(firstnumber) # возвращаем нод



def nok(firstnumber, secondnumber):
	if type(firstnumber) != type(1) or type(secondnumber) != type(1):
		return('Введите целое число')

	a = firstnumber
	b = secondnumber

	if a == 0 or b == 0:
		return('Не найти нок, введите число не равное нулю')

	while b != 0:
		a, b = b, a % b
		 
	return(firstnumber * secondnumber // a)
	# возвращаем нок по формуле


if __name__ == '__main__':
	print(nod(11, 22))
	print(nok(22, 44))