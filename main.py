from field import Field, Point, Colors
from robots import UserRobot, SampleRobot

exercise_options = {
    'start_x': 0,
    'start_y': 0,

    'field_width': 8,
    'field_height': 10,

    'run_options': {'height': 3, 'width': 7},
    'max_steps': 100
}

field = Field(exercise_options['field_height'], exercise_options['field_width'])

user_robot = UserRobot('user_robot', field,
                       Point(exercise_options['start_x'], exercise_options['start_y']), Colors.BLUE)

sample_robot = SampleRobot('sample robot', field,
                           Point(exercise_options['start_x'], exercise_options['start_y']), Colors.RED)

user_robot.act(exercise_options['run_options'])
sample_robot.act(exercise_options['run_options'])

# correct = validate(field)

print()

print('Field:')
print(field)
