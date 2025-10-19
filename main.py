clear()
change_hat(Hats.Purple_Hat)

from smart_move import smart_move
from smart_plant import smart_plant

while True:
	if can_harvest():
		harvest()

	smart_plant()

	smart_move()
