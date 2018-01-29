from os import getcwd
from base.field import Point
from multiplayer.mp_runner import run_robots

if __name__ == "__main__":
    exercise_opts = {
        'start': Point(0, 0),

        'field_width': 8,
        'field_height': 10,

        'run_options': {'height': 3, 'width': 7},
        'max_steps': 100
    }

    pwd = getcwd()
    target_dir = pwd if pwd.endswith('multiplayer') else pwd + '/multiplayer'

    run_robots(exercise_opts)
