from base.robot import Robot


def adapt_run(robot: Robot, exercise_options, run_robot) -> None:
    run_robot(robot, exercise_options['width'], exercise_options['height'])
