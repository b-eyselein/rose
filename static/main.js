function domReady(callback) {
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', callback);
    }
    else {
        callback();
    }
}
const FIELD_COUNT_X = 10;
const FIELD_COUNT_Y = 10;
domReady(() => {
    const mainCanvas = document.querySelector('#mainCanvas');
    const ctx = mainCanvas.getContext("2d");
    const drawWidth = mainCanvas.width;
    const drawHeight = mainCanvas.height;
    const fieldWidthX = drawWidth / FIELD_COUNT_X;
    const fieldWidthY = drawWidth / FIELD_COUNT_Y;
    for (let i = 1; i < FIELD_COUNT_X; i++) {
        ctx.moveTo(i * fieldWidthX, 0);
        ctx.lineTo(i * fieldWidthX, drawHeight);
        ctx.stroke();
    }
    for (let i = 1; i < FIELD_COUNT_Y; i++) {
        ctx.moveTo(0, i * fieldWidthY);
        ctx.lineTo(drawWidth, i * fieldWidthY);
        ctx.stroke();
    }
});
