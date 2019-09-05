from typing import List

from flask import Flask, render_template
from pathlib import Path

app = Flask(__name__)


@app.route('/')
def route_index():
    example_exes: List[Path] = [p for p in list((Path.cwd() / 'exercises').iterdir())]

    example_ex_names: List[str] = [p.name for p in example_exes]

    return render_template('index.html', exercises=example_ex_names)


if __name__ == "__main__":
    app.debug = True
    app.run(port=5050)
