
def get_last_number(file):
	"""
	Takes a file as paramether and prints the last number that the 
	sheep see before falling asleep for each number in the file
	"""
	inputs_numbers = [int(n.rstrip()) for n in open(file)]

	for case, number in enumerate(inputs_numbers[1:], 1):
		is_sleep = False
		tmp_numbers = [n for n in range(10)]
		i = 1
		
		if number == 0:
			print("CASE #{}: {}".format(case, 'INSOMNIA'))
			continue
		
		current_number = number	
		
		while not is_sleep:
			for digit in str(current_number):
				if int(digit) in tmp_numbers:
					tmp_numbers.remove(int(digit))
			
			if tmp_numbers:
				i += 1
				current_number = number * i
			else:
				is_sleep = True
			
		if is_sleep:
			print("CASE #{}: {}".format(case, current_number))

if __name__ == '__main__':
	print('-- file c-input.in --')
	get_last_number('c-input.in')
	print('-- file 5_cases.in --')
	get_last_number('5_cases.in')
