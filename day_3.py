from operator import itemgetter

file_name = 'files/day_3.txt'
with open(file_name, 'r') as f:
	lines = list(map(lambda s: s.strip(), f.readlines()))
	lines = lines[0:-1]


def part_one():
	print(lines)
	lines_array = list(map(list, lines))
	print(lines_array)

	length = len(lines[0])
	columns = list()
	for i in range(length):
		# column = list(map(itemgetter(0), lines_array))  # or
		column = [item[i] for item in lines_array]
		column = ''.join(column)
		columns.append(column)
	columns = [''.join([line[i] for line in lines_array]) for i in range(length)]  # One liner version
	print(columns)
	"""
	The end result is gamma * epsilon.  
	If number of ones and zeroes is equal either one can be the most common.
	"""
	result_string = ''.join(list(map(lambda x: '1' if x.count('1') > x.count('0') else '0', columns)))
	result = int(result_string, 2)
	result_complement = result ^ int('1' * length, 2)
	print(result)
	print(result_complement)
	return result * result_complement


def part_one_short():
	length = len(lines[0])
	result = int(''.join(list(map(lambda x: '1' if x.count('1') > x.count('0') else '0', [''.join([line[i] for line in list(map(list, lines))]) for i in range(length)]))), 2)
	return result * (result ^ int('1' * length, 2))


def part_two():
	pass


if __name__ == '__main__':
	result_one = part_one_short()
	print(f"Result one: {result_one}")
	part_two()
