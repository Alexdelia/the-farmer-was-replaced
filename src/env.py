def create():
	return {
		"size": get_world_size(),  #
		"x": 0,
		"y": 0,
	}


def update(e):
	pass


# get_pos_x() and get_pos_y() takes 1 tick to execute
def go(e, dir):
	if dir == North:
		e["y"] += 1
	elif dir == East:
		e["x"] += 1
	elif dir == South:
		e["y"] -= 1
	else:
		e["x"] -= 1

	move(dir)
