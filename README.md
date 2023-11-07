# 2D-Space-Game

A simple shooting game created using Pygame. The player controls a spaceship and must shoot down incoming enemies while avoiding collisions with them. The objective is to score as many points as possible before an enemy reaches the bottom of the screen.

https://user-images.githubusercontent.com/108623726/221308126-9277929f-0356-48b1-9a3e-8088c5cc0245.mp4

## Game Overview

In this shooting game, you control a spaceship at the bottom of the screen and must shoot down the incoming enemies. The game continues until an enemy reaches the bottom of the screen, resulting in a game over.

## Prerequisites

Before you begin, ensure you have Python and the Pygame library installed on your computer. You can install Pygame using the following command:

```bash
pip install pygame
```

## Installation

1. Clone this repository or download the source code.

```bash
git clone https://github.com/arham-kk/2D-Space-Game.git
cd 2D-Space-Game
```

2. Make sure you have the game assets in a folder named `assets` within the game directory. You can use your own assets or download the provided ones from [here](assets/).

3. Run the game:

```bash
python game.py
```

## How to Play

- Launch the game, and you will control a spaceship at the bottom of the screen.
- Use the arrow keys to move your spaceship left, right, up, and down.
- Press the spacebar to shoot projectiles at the enemies.
- Your objective is to shoot down as many enemies as possible and score points.
- The game continues until an enemy reaches the bottom of the screen, resulting in a game over.

## Controls

- Left Arrow Key: Move the spaceship to the left.
- Right Arrow Key: Move the spaceship to the right.
- Up Arrow Key: Move the spaceship upwards.
- Down Arrow Key: Move the spaceship downwards.
- Spacebar: Shoot projectiles.

## Gameplay

- Enemies will continuously spawn from the top of the screen and move downward.
- Your goal is to shoot down these enemies using your spaceship's projectiles.
- Avoid colliding with enemies or letting them reach the bottom of the screen, as this will result in a game over.
- The game continues until you decide to exit or until an enemy reaches the bottom.

## Scoring

- You earn 10 points for each enemy you shoot down.
- The current score is displayed in the top-left corner of the game window.
- Try to achieve the highest score possible!

## Assets

The game uses the following assets, which should be placed in a folder named `assets`:

- Player spaceship image: `player.png`
- Enemy spaceship image: `enemy.png`
- Projectile image: `projectile.png`
- Explosion image: `blast.png`
- Bullet sound effect: `bullet.wav`
- Explosion sound effect: `explosion.wav`
- Game over image: `gameover.png`
- Game over sound effect: `gameover.mp3`

- Player, enemy, projectile, and explosion images: Freepik.com
- Bullet and explosion sounds: mixkit.co

Please make sure you have these assets in the `assets` folder within the game directory.

## License

This game is available under the [MIT License](LICENSE).

Have fun playing the Shooting Game!