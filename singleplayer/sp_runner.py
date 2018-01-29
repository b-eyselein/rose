from json import dumps as json_dump

from base.field import Field, Colors
from singleplayer.sp_solution import *
from singleplayer.sp_validation import validate


def run_robots(target_dir: str, exercise_options: Dict):
    # Inst. fields for both robots
    user_field = Field(exercise_options['field_height'], exercise_options['field_width'])
    sample_field = Field(exercise_options['field_height'], exercise_options['field_width'])

    # Inst. robots
    user_robot = UserRobot('user_robot', user_field, exercise_options['start'], Colors.BLUE)
    sample_robot = SampleRobot('sample_robot', sample_field, exercise_options['start'], Colors.RED)

    user_robot.run(exercise_options['run_options'])
    sample_robot.run(exercise_options['run_options'])

    result: Dict = {
        'correct': validate(user_field, sample_field),
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
    with open(target_dir + '/actions.json', 'w+') as actions_file:
        actions_file.write(json_dump(result, indent=2))
