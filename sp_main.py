#!/usr/bin/env python3

import json
from typing import Dict

from solution import *

from base.field import Field, Colors
from base.field import Point
from sp_validation import validate


def run_robots(exercise_options: Dict):
    start_coordinates = exercise_options['start']
    start = Point(start_coordinates['x'], start_coordinates['y'])

    field_options = exercise_options['field']
    field_height = field_options['height']
    field_width = field_options['width']

    sample_field = Field(field_height, field_width)
    sample_robot = SampleRobot('sample_robot', sample_field, start, Colors.RED)
    sample_robot.run(*exercise_options['run_options'])

    # Inst. fields for both robots
    user_field = Field(field_height, field_width)
    user_robot = UserRobot('user_robot', user_field, start, Colors.BLUE)
    user_robot.run(*exercise_options['run_options'])

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
        actions_file.write(json.dumps(result, indent=2))


if __name__ == "__main__":
    with open('options.json', 'r') as file:
        exercise_opts = json.loads(file.read())

        run_robots(exercise_opts)
