from json import load as json_load
from pathlib import Path
from typing import List

from flask import Flask, render_template, url_for, redirect, jsonify

app = Flask(__name__)

exercises_dir: Path = Path.cwd() / 'exercises'


@app.route('/')
def route_index():
    example_exes: List[Path] = [p for p in exercises_dir.iterdir()]

    example_ex_names: List[str] = [p.name for p in example_exes]

    return render_template('index.html', exercises=example_ex_names)


@app.route('/<string:exercise_name>')
def route_exercise(exercise_name: str):
    exercise_dir: Path = exercises_dir / exercise_name

    if not exercise_dir.exists():
        return redirect(url_for('route_index'))

    return render_template('exercise.html', exercise_name=exercise_name)


@app.route('/<string:exercise_name>/options')
def route_exercise_options(exercise_name: str):
    options_file: Path = exercises_dir / exercise_name / 'options.json'

    if not options_file.exists():
        return redirect(url_for('route_index'))

    return jsonify(json_load(options_file.open()))


@app.route('/<string:exercise_name>/simulate')
def route_simulate(exercise_name: str):
    pass


if __name__ == "__main__":
    app.debug = True
    app.run(port=5050)
