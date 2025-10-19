from config import plant_order, plant_order_len, pumpkin_size
from smart_tile import smart_tile


def get_index():
	return (get_pos_y() * (plant_order_len + 1)) + get_pos_x()


def is_pumpkin():
	x = get_pos_x()
	y = get_pos_y()
	size = get_world_size()
	block_row = x // pumpkin_size
	block_col = y // pumpkin_size
	return (block_row + block_col) % 2 == 0


def smart_plant():
	if is_pumpkin():
		smart_tile()
		plant(Entities.Pumpkin)
		return

	i = get_index()

	p = plant_order[i % plant_order_len]
	if not p:
		return

	if p == Entities.Carrot:
		smart_tile()

	plant(p)
