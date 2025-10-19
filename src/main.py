clear()
change_hat(Hats.Carrot_Hat)

import env
from smart_move import smart_move
from smart_plant import smart_plant

e = env.create()

while True:
	env.update(e)

	if can_harvest():
		harvest()

	smart_plant(e)

	smart_move(e)
