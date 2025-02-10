# Car Racing Game (Flask + Pygame)

## Description
This is a simple car racing game built using **Pygame** for game mechanics and **Flask** to serve it as a web application. The game involves controlling a car on a road while avoiding obstacles (hurdles). The speed increases over time to enhance difficulty, and the game ends if the car collides with an obstacle.

## Features
- **Smooth Car Movement** – Control the car using arrow keys.
- **Dynamic Road and Hurdles** – Moving background and randomly appearing obstacles.
- **Collision Detection** – Game ends when the car hits a hurdle.
- **Score Tracking** – Score increases as the game progresses.
- **Flask Integration** – Run the game in a web browser.

## Installation & Setup
### Prerequisites
Ensure you have Python installed. You can check by running:
```bash
python --version
```

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourGostCompiler/car-racing-flask.git
cd car-racing-flask
```

### Step 2: Set Up a Virtual Environment 
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Step 3: Run the Flask App
```bash
python app.py
```

### Step 4: Open in Browser
Visit `http://127.0.0.1:5000` in your web browser to start playing the game.

## File Structure
```
car-racing-flask/
│── app.py               # Flask Backend
│── game.py              # Pygame logic
│── requirements.txt     # Dependencies
│── README.md            # Project Documentation
│── static/
│   ├── assets/          # Car, road, and hurdle images
│   ├── css/
│   │   ├── style.css    # Game styling
│   ├── js/
│   │   ├── game.js      # JavaScript for interactivity
│── templates/
│   ├── index.html       # Game interface
```

## Controls
- **Left Arrow (`←`)** – Move car left
- **Right Arrow (`→`)** – Move car right
- **Up Arrow (`↑`)** – Accelerate
- **Down Arrow (`↓`)** – Decelerate

## Future Improvements
- Add a leaderboard for high scores.
- Implement different difficulty levels.
- Mobile responsiveness.

Happy Racing! 🏎️💨
