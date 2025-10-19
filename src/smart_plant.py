from config import plant_order, plant_order_len, pumpkin_size
from smart_tile import smart_tile


def get_index(e):
	return (e["y"] * (plant_order_len + 1)) + e["x"]


def is_pumpkin(e):
	block_row = e["x"] // pumpkin_size
	block_col = e["y"] // pumpkin_size
	return (block_row + block_col) % 2 == 0


def smart_plant(e):
	if is_pumpkin(e):
		smart_tile()
		plant(Entities.Pumpkin)
		return

	i = get_index(e)

	p = plant_order[i % plant_order_len]
	if not p:
		return

	if p == Entities.Carrot:
		smart_tile()

	plant(p)
