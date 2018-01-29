from json import dumps as json_dump
from os import getcwd
from typing import Dict

from base.field import Field, Colors
from base.field import Point
from multiplayer.mp_solution import UserRobot, SampleRobot

max_steps = 100


def run_robots(exercise_options: Dict):
    # Inst. fields for both robots
    field = Field(exercise_options['field_height'], exercise_options['field_width'])

    # Inst. robots
    user_robot = UserRobot('user_robot', field, exercise_options['start'], Colors.BLUE)
    sample_robot = SampleRobot('sample_robot', field, exercise_options['start'], Colors.RED)

    for step_count in range(max_steps):
        user_robot.act(exercise_options['run_options'])
        sample_robot.act(exercise_options['run_options'])

    result: Dict = {
        'correct': False,  # validate(user_field, sample_field),
        'user': {
            'name': user_robot.name,
            'start': str(user_robot.initial_position),
            'actions_size': len(user_robot.actions),
            'actions': list(map(str, user_robot.actions))
        },
        'sample': {
            'name': sample_robot.name,
            'start': str(sample_robot.initial_position),
            'size': len(sample_robot.actions),
            'actions': list(map(str, sample_robot.actions))
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

    pwd = getcwd()
    target_dir = pwd if pwd.endswith('multiplayer') else pwd + '/multiplayer'

    run_robots(exercise_opts)
