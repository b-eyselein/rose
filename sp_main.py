#!/usr/bin/env python3

from json import loads as json_loads, dumps as json_dumps
from typing import Dict

from base.field import Field, Colors, Point
from base.robot import Robot
from sample_robot import run_sample_robot
from solution_robot import run_user_robot
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

    sample_field: Field = Field(field_height, field_width)
    sample_robot: Robot = Robot('sample_robot', sample_field, start, Colors.RED)
    run_sample_robot(sample_robot, *exercise_options['run_options'])

    user_field: Field = Field(field_height, field_width)
    user_robot: Robot = Robot('user_robot', user_field, start, Colors.BLUE)
    run_user_robot(user_robot, *exercise_options['run_options'])

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
        actions_file.write(json_dumps(result))


if __name__ == "__main__":
    with open('options.json', 'r') as file:
        exercise_opts = json_loads(file.read())

        run_robots(exercise_opts)
