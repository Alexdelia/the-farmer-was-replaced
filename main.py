clear()
change_hat(Hats.Purple_Hat)

from smart_move import smart_move

while True:
	if can_harvest():
		harvest()

	if get_pos_y() % 3 == 0:
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Carrot)
	elif get_pos_y() % 3 == 1:
		plant(Entities.Bush)

	smart_move()
