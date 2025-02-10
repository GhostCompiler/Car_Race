from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start-game")
def start_game():
    # Run the Pygame script
    subprocess.Popen(["python3", "game.py"])
    return "Game started! Check the game window."

if __name__ == "__main__":
    app.run(debug=True)
