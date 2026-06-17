const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

// Tamaño del canvas
canvas.width = window.innerWidth - 160;
canvas.height = window.innerHeight;

let p0 = null;

// Sliders
const rSlider = document.getElementById('r');
const gSlider = document.getElementById('g');
const bSlider = document.getElementById('b');
const sizeSlider = document.getElementById('size');

// Actualizar preview de color y valores
function updatePreview() {
    const r = rSlider.value;
    const g = gSlider.value;
    const b = bSlider.value;
    document.getElementById('r-val').textContent = r;
    document.getElementById('g-val').textContent = g;
    document.getElementById('b-val').textContent = b;
    document.getElementById('size-val').textContent = sizeSlider.value;
    document.getElementById('color-preview').style.background =
        `rgb(${r},${g},${b})`;
}

rSlider.addEventListener('input', updatePreview);
gSlider.addEventListener('input', updatePreview);
bSlider.addEventListener('input', updatePreview);
sizeSlider.addEventListener('input', updatePreview);

// Click en el canvas
canvas.addEventListener('click', (e) => {
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    if (p0 === null) {
        p0 = { x, y };
    } else {
        const p1 = { x, y };
        drawLine(p0, p1);
        p0 = null;
    }
});

// Llamada a Flask y dibujo
async function drawLine(p0, p1) {
    const response = await fetch('/draw', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            x0: p0.x, y0: p0.y,
            x1: p1.x, y1: p1.y,
            r: parseInt(rSlider.value),
            g: parseInt(gSlider.value),
            b: parseInt(bSlider.value),
            size: parseInt(sizeSlider.value)
        })
    });

    const pixels = await response.json();
    pixels.forEach(pixel => {
        ctx.fillStyle = pixel.color;
        ctx.fillRect(pixel.x, pixel.y, pixel.size, pixel.size);
    });
}

// Limpiar canvas
function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    p0 = null;
}

// Atajo teclado C
document.addEventListener('keydown', (e) => {
    if (e.key === 'c') clearCanvas();
});

updatePreview();