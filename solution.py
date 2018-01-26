from typing import Dict
from robots import SingleActorRobot


class UserRobot(SingleActorRobot):
    def run(self, options: Dict):
        height = options['height']
        width = options['width']
        for h in range(height - 1):
            self.mark()
            self.go_up()

        for w in range(width - 1):
            self.mark()
            self.go_right()

        for h in range(height - 1):
            self.mark()
            self.go_down()

        for w in range(width - 1):
            self.mark()
            self.go_left()
