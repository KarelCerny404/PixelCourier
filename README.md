# Pixel Courier
*A very simple game made in pygame*

## What it's about
You pick up small colorful cubes (*pixels*) and deliver them to houses of same color as the pixel, each successful delivery gives you one score point. After each delivery, another cube of the same color spawns and is waiting to be delivered again. It isn't as easy however, because there are walls randomly spawning around all the map. If you hit the wall, you get teleported to the spawn point. With each score point there is one more wall spawning around, so your unpicked pixels can easily get trapped in by the walls. When there's nothing to do (all pixels are trapped and you have none in your inventory) you have to surrender. If you surrender with 25 or more score points, it's considered a win, otherwise it's game over. Note that sometimes it might not even be possible to get 25 points as the wall placement resets to random with each delivered pixel, but pixels on the ground don't. You also can shrink yourself to a minimum size of 2 by 2 pixels to better fit inside the walls

## Features (for HC YSWS)
- Score points
- Shrinking of player
- Win/game over screen
- Reset of the game

## Controls
- Arrow keys: moving player around
- `N`: Grow the player
- `M`: Shrink the player
- `S`: Surrender, end the game
- `R`*(on the win/game over screen)*: Reset, play again

## Screenshot
![https://github.com/KarelCerny404/PixelCourier/blob/e8510b049b089b51150baff0f7dc61698ff38726/assets/screenshot.png](Screenshot)