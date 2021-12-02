with open('files/day_1.txt', 'r') as f:
	lines = list(map(int, f.readlines()))

SLIDING_WINDOW_SIZE = 3


def part_one():
	counter = 0
	for i in range(1, len(lines)):
		if lines[i - 1] < lines[i]:
			counter += 1
			print(f"{lines[i]} (increased)")
		else:
			print(f"{lines[i]} (decreased)")
	print(f"Number of measurements larger than the previous: {counter}")


def sliding_window_sum(array, index, window_size):
	print(f"{array[index: index + window_size]} = {sum(array[index: index + window_size])}")
	return sum(array[index: index + window_size])


def part_two():
	counter = 0
	for i in range(1, len(lines)):
		if sliding_window_sum(lines, i - 1, SLIDING_WINDOW_SIZE) < \
				sliding_window_sum(lines, i, SLIDING_WINDOW_SIZE):
			counter += 1
			print(f"{sliding_window_sum(lines, i, SLIDING_WINDOW_SIZE)} (increased)")
		else:
			print(f"{sliding_window_sum(lines, i, SLIDING_WINDOW_SIZE)} (decreased)")
	print(f"Number of measurements larger than the previous: {counter}")


if __name__ == '__main__':
	part_one()
	part_two()
