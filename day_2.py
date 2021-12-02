from enum import Enum

with open('files/day_2.txt', 'r') as f:
	lines = list(map(lambda x: str(x).strip(), f.readlines()))


class Direction(Enum):
	forward = 'forward'
	down = 'down'
	up = 'up'
	aim = 'aim'


def part_one():
	horizontal_position = 0
	depth = 0
	for l in lines:
		if l.isspace() or len(l) == 0: continue
		direction, amount = l.split()
		amount = int(amount)
		if direction == Direction.forward.name:
			horizontal_position += amount
		else:
			depth += amount if direction == Direction.down.name else -amount
	print(f"{horizontal_position} * {depth} = {horizontal_position * depth}")


def part_two():
	horizontal_position = 0
	depth = 0
	aim = 0
	for l in lines:
		if l.isspace() or len(l) == 0: continue
		direction, amount = l.split()
		amount = int(amount)
		if direction == Direction.forward.name:
			horizontal_position += amount
			depth += aim * amount
		else:
			aim += amount if direction == Direction.down.name else -amount
	print(f"{horizontal_position} * {depth} = {horizontal_position * depth}")


if __name__ == '__main__':
	part_one()
	part_two()
