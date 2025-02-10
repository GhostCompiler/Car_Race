const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

canvas.width = 800;
canvas.height = 600;

const carImg = new Image();
carImg.src = "static/assets/car_nfs.png";

const roadImg = new Image();
roadImg.src = "static/assets/road_nfs.jpg";

let car = {
    x: canvas.width / 2 - 40,
    y: canvas.height - 100,
    width: 80,
    height: 160,
    speed: 5
};

let hurdles = [];
let score = 0;

// Move the car
document.addEventListener("keydown", function(event) {
    if (event.key === "ArrowLeft" && car.x > 50) car.x -= car.speed;
    if (event.key === "ArrowRight" && car.x < canvas.width - car.width - 50) car.x += car.speed;
});

// Hurdle class
class Hurdle {
    constructor() {
        this.x = Math.random() * (canvas.width - 50);
        this.y = -50;
        this.width = 50;
        this.height = 50;
        this.speed = 5;
    }

    move() {
        this.y += this.speed;
    }

    draw() {
        ctx.fillStyle = "red";
        ctx.fillRect(this.x, this.y, this.width, this.height);
    }
}

// Game loop
function updateGame() {
    ctx.drawImage(roadImg, 0, 0, canvas.width, canvas.height);
    ctx.drawImage(carImg, car.x, car.y, car.width, car.height);

    if (Math.random() < 0.02) {
        hurdles.push(new Hurdle());
    }

    for (let i = 0; i < hurdles.length; i++) {
        hurdles[i].move();
        hurdles[i].draw();

        if (hurdles[i].y > canvas.height) {
            hurdles.splice(i, 1);
            score++;
        }

        // Collision detection
        if (
            car.x < hurdles[i].x + hurdles[i].width &&
            car.x + car.width > hurdles[i].x &&
            car.y < hurdles[i].y + hurdles[i].height &&
            car.y + car.height > hurdles[i].y
        ) {
            alert("Game Over! Your Score: " + score);
            document.location.reload();
        }
    }

    requestAnimationFrame(updateGame);
}

updateGame();
