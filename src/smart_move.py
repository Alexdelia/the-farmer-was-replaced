from env import go


def smart_move(e):
	size = e["size"]
	x = e["x"]
	y = e["y"]

	# bottom row
	if y == 0 and x != 0:
		go(e, West)
		return

	# second bottom row
	if y == 1 and x % 2 == 1 and x != size - 1:
		go(e, East)
		return

	# left col
	if y == 0 and x != size - 1:
		go(e, North)
		return

	# top row
	if y == size - 1 and x % 2 == 0:
		go(e, East)
		return

	if x % 2 == 0:
		go(e, North)
	else:
		go(e, South)
