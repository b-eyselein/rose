function domReady(callback) {
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', callback);
    }
    else {
        callback();
    }
}
function loadExerciseOptions(exerciseName) {
    fetch(`/${exerciseName}/options`)
        .then((response) => response.json())
        .then((exerciseOptions) => drawField(exerciseOptions));
}
function drawField(exerciseOptions) {
    const mainCanvas = document.querySelector('#mainCanvas');
    const ctx = mainCanvas.getContext("2d");
    const drawWidth = mainCanvas.width;
    const drawHeight = mainCanvas.height;
    const fieldWidthX = drawWidth / exerciseOptions.field.height;
    const fieldWidthY = drawWidth / exerciseOptions.field.width;
    ctx.lineWidth = 1;
    for (let i = 1; i < exerciseOptions.field.height; i++) {
        ctx.moveTo(i * fieldWidthX, 0);
        ctx.lineTo(i * fieldWidthX, drawHeight);
        ctx.stroke();
    }
    for (let i = 1; i < exerciseOptions.field.width; i++) {
        ctx.moveTo(0, i * fieldWidthY);
        ctx.lineTo(drawWidth, i * fieldWidthY);
        ctx.stroke();
    }
}
domReady(() => {
    const exerciseName = document.querySelector('#exerciseName').value;
    loadExerciseOptions(exerciseName);
});
