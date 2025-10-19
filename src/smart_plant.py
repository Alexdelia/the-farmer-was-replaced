from plant_order import plant_order

plant_order_len = len(plant_order)


def get_index():
	return (get_pos_y() * (get_world_size() + 1)) + get_pos_x()


def smart_plant():
	i = get_index()

	p = plant_order[i % plant_order_len]
	if not p:
		return

	if p == Entities.Carrot and get_ground_type() == Grounds.Grassland:
		till()

	plant(p)
