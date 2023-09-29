class Robot:
    def __init__(self):
        self._pos = [0, 0]
        self._vel = [0, 0]
        self._acc = [0, 0]
        self._yaw = 0

    def print(self):
        print(f"pos={self._pos}, vel={self._vel}, acc={self._acc}, yaw={self._yaw}")

    def move(self, delta_x, delta_y, delta_yaw, dt):
        """Move the robot by the given amount.

        :param delta_x: The amount to move in the x direction.
        :param delta_y: The amount to move in the y direction.
        :param dt: The amount of time to move.
        """
        new_vel = [delta_x / dt, delta_y / dt]
        self._acc = [(new_vel[0] - self._vel[0]) / dt, (new_vel[1] - self._vel[1]) / dt]
        self._vel = new_vel
        self._pos = [self._pos[0] + delta_x, self._pos[1] + delta_y]
        self._yaw += delta_yaw


if __name__ == "__main__":
    robot = Robot()
    robot.print()
    robot.move(0.5, 3, 0.1, 0.1)
    robot.print()
