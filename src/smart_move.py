def smart_move():
	size = get_world_size()
	x = get_pos_x()
	y = get_pos_y()

	# bottom row
	if y == 0 and x != 0:
		move(West)
		return

	# second bottom row
	if y == 1 and x % 2 == 1 and x != size - 1:
		move(East)
		return

	# left col
	if y == 0 and x != size - 1:
		move(North)
		return

	# top row
	if y == size - 1 and x % 2 == 0:
		move(East)
		return

	if x % 2 == 0:
		move(North)
	else:
		move(South)
