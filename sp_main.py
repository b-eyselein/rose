#!/usr/bin/env python3

import json
from typing import Dict

from solution import *

from base.field import Field, Colors
from base.field import Point
from sp_validation import validate


def dump_robot(robot: Robot) -> Dict:
    return {
        'name': robot.name,
        'actions_size': len(robot.actions),
        'actions': list(map(str, robot.actions))
    }


def run_robots(exercise_options: Dict):
    start_coordinates = exercise_options['start']
    start = Point(start_coordinates['x'], start_coordinates['y'])

    field_options = exercise_options['field']
    field_height: int = int(field_options['height'])
    field_width: int = int(field_options['width'])

    sample_field = Field(field_height, field_width)
    sample_robot = SampleRobot('sample_robot', sample_field, start, Colors.RED)
    sample_robot.run(*exercise_options['run_options'])

    user_field = Field(field_height, field_width)
    user_robot = UserRobot('user_robot', user_field, start, Colors.BLUE)
    user_robot.run(*exercise_options['run_options'])

    result: Dict = {
        'correct': validate(user_field, sample_field),
        'start': {
            'x': sample_robot.initial_position.x,
            'y': sample_robot.initial_position.y
        },
        'sample': dump_robot(sample_robot),
        'user': dump_robot(user_robot)
    }

    # Write result to json file
    with open('actions.json', 'w+') as actions_file:
        actions_file.write(json.dumps(result))


if __name__ == "__main__":
    with open('options.json', 'r') as file:
        exercise_opts = json.loads(file.read())

        run_robots(exercise_opts)
