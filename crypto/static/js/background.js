const canvas = document.getElementById("cryptoCanvas");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const particles = [];

class Particle {
  constructor(x, y, speedX, speedY, size) {
    this.x = x;
    this.y = y;
    this.speedX = speedX;
    this.speedY = speedY;
    this.size = size;
    this.alpha = Math.random();
  }

  draw() {
    ctx.globalAlpha = this.alpha;
    ctx.fillStyle = `rgba(0, 255, 150, ${this.alpha})`;
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
    ctx.closePath();
    ctx.fill();
  }

  update() {
    this.x += this.speedX;
    this.y += this.speedY;
    this.alpha -= 0.005;

    if (this.alpha <= 0 || this.size <= 0) {
      this.reset();
    }
  }

  reset() {
    this.x = Math.random() * canvas.width;
    this.y = Math.random() * canvas.height;
    this.speedX = (Math.random() - 0.5) * 2;
    this.speedY = (Math.random() - 0.5) * 2;
    this.size = Math.random() * 3 + 1;
    this.alpha = Math.random();
  }
}

function initParticles(num) {
  for (let i = 0; i < num; i++) {
    particles.push(
      new Particle(
        Math.random() * canvas.width,
        Math.random() * canvas.height,
        (Math.random() - 0.5) * 2,
        (Math.random() - 0.5) * 2,
        Math.random() * 3 + 1
      )
    );
  }
}

function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  particles.forEach((particle) => {
    particle.update();
    particle.draw();
  });
  requestAnimationFrame(animate);
}

initParticles(200);
animate();

window.addEventListener("resize", () => {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  particles.length = 0;
  initParticles(200);
});
