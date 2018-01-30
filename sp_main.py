from json import dumps as json_dump
from typing import Dict

from solution import *

from base.field import Field, Colors
from base.field import Point
from sp_validation import validate


def run_robots(exercise_options: Dict):
    sample_field = Field(exercise_options['field_height'], exercise_options['field_width'])
    sample_robot = SampleRobot('sample_robot', sample_field, exercise_options['start'], Colors.RED)
    sample_robot.run()

    # Inst. fields for both robots
    user_field = Field(exercise_options['field_height'], exercise_options['field_width'])
    user_robot = UserRobot('user_robot', user_field, exercise_options['start'], Colors.BLUE)
    user_robot.run()

    result: Dict = {
        'correct': validate(user_field, sample_field),
        'start': {
            'x': sample_robot.initial_position.x,
            'y': sample_robot.initial_position.y
        },
        'sample': {
            'name': sample_robot.name,
            'size': len(sample_robot.actions),
            'actions': list(map(str, sample_robot.actions))
        },
        'user': {
            'name': user_robot.name,
            'actions_size': len(user_robot.actions),
            'actions': list(map(str, user_robot.actions))
        }
    }

    # Write result to json file
    with open('actions.json', 'w+') as actions_file:
        actions_file.write(json_dump(result, indent=2))


if __name__ == "__main__":
    exercise_opts = {
        'start': Point(0, 0),

        'field_width': 8,
        'field_height': 10,

        'run_options': {'height': 3, 'width': 7},
        'max_steps': 100
    }

    run_robots(exercise_opts)
