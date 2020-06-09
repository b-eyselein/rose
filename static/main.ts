function domReady(callback: () => void): void {
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', callback);
    } else {
        callback();
    }
}

interface ExerciseOptions {
    field: {
        height: number;
        width: number;
    }
    start: {
        x: number;
        y: number;
    }
    run_options: number[];
}

function loadExerciseOptions(exerciseName: string): void {
    fetch(`/${exerciseName}/options`)
        .then((response) => response.json())
        .then((exerciseOptions: ExerciseOptions) => drawField(exerciseOptions));
}

function drawField(exerciseOptions: ExerciseOptions): void {
    const mainCanvas = document.querySelector<HTMLCanvasElement>('#mainCanvas');
    const ctx: CanvasRenderingContext2D = mainCanvas.getContext("2d");

    const drawWidth: number = mainCanvas.width;
    const drawHeight: number = mainCanvas.height;

    const fieldWidthX: number = drawWidth / exerciseOptions.field.height;
    const fieldWidthY: number = drawWidth / exerciseOptions.field.width;

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
    const exerciseName: string = document.querySelector<HTMLInputElement>('#exerciseName').value;

    loadExerciseOptions(exerciseName);
});