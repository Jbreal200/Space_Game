# Space Simulation

A gravity simulation application built with Python and Pygame. This project demonstrates orbital mechanics and gravitational physics in an interactive 2D environment.

## Project Description

The Space Simulation allows you to launch spacecraft and watch them orbit around a planet under the influence of gravity. The application features:

- **Interactive Spacecraft Launch**: Click to set launch position, then click again to set velocity
- **Realistic Gravity Physics**: Objects follow gravitational physics laws with accurate force calculations
- **Orbital Visualization**: Visual trails show the path of each spacecraft
- **Collision Detection**: Detects crashes with the planet and objects leaving the simulation area
- **Audio**: Background music plays during simulation
- **Orbital Status**: Objects display an "IN ORBIT" label when they've been in orbit for 8+ seconds

## Features

- Dynamic gravity calculations using Newton's law of universal gravitation
- Real-time spacecraft physics simulation
- Visual feedback with orbital trails
- Collision detection and removal of out-of-bounds objects
- Interactive mouse-based controls

## Requirements

- Python 3.13+
- pygame 2.6.0+

## Installation

To install the required dependencies, run:

```bash
pip install pygame
```
## Project Files

- `main.py` - Main gravity simulation application with interactive spacecraft launching
- `test.py` - Test/demo application
- `rocket.png` - Spacecraft image asset
- `Earth.png` - Planet image asset
- `Background.jpg` - Background image for the simulation
- `Music.wav` - Background music file
- `Sample.wav` - Audio file for test demo

## How to Use

1. **Run the main simulation**:
   ```bash
   python main.py
   ```

2. **Launch a spacecraft**:
   - Click anywhere on the screen to set the launch position
   - Click a second location to set the velocity (the line shows the direction)
   - The spacecraft will launch and follow the gravitational pull of the planet

3. **Observe the simulation**:
   - Watch the colored orbital trail as the spacecraft moves
   - If it stays in orbit for 8+ seconds, it will display "IN ORBIT"
   - Objects that crash into the planet or leave the screen are removed


## Game Mechanics

- **Gravity**: Objects are attracted to the planet using the gravitational force formula
- **Velocity**: Initial velocity is determined by the distance and direction of your second click
- **Orbital Status**: Objects become labeled as "IN ORBIT" after 8 seconds on screen
- **Collision**: Crashing into the planet or leaving the game area removes the object

## Controls

- **Left Mouse Button**: Set launch position (first click) or velocity direction (second click)
- **Close Window**: Exit the simulation

