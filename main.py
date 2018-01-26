from field import Field, Point, Colors
from sample import SampleRobot
from solution import UserRobot
from validation import validate
from typing import Dict
import json

exercise_options = {
    'start_x': 0,
    'start_y': 0,

    'field_width': 8,
    'field_height': 10,

    'run_options': {'height': 3, 'width': 7},
    'max_steps': 100
}

user_field = Field(exercise_options['field_height'], exercise_options['field_width'])
sample_field = Field(exercise_options['field_height'], exercise_options['field_width'])

user_robot = UserRobot('user_robot', user_field,
                       Point(exercise_options['start_x'], exercise_options['start_y']), Colors.BLUE)

sample_robot = SampleRobot('sample_robot', sample_field,
                           Point(exercise_options['start_x'], exercise_options['start_y']), Colors.RED)

with open('actions.txt', 'w+') as actions_file:
    user_robot.run(exercise_options['run_options'])
    sample_robot.run(exercise_options['run_options'])

    correct = validate(user_field, sample_field)

    print('Field:')
    print(user_field)

    result: Dict = {
        'user': {
            'name': user_robot.name,
            'start': str(user_robot.initial_position),
            'actions_size': len(user_robot.actions),
            'actions': list(map(str, user_robot.actions))
        },
        # 'user_result': str(user_field),
        'sample': {
            'name': sample_robot.name,
            'start': str(sample_robot.initial_position),
            'size': len(sample_robot.actions),
            'actions': list(map(str, sample_robot.actions))
        },
        # 'sample_result': str(sample_field)
    }

    actions_file.write(json.dumps(result, indent=2))
