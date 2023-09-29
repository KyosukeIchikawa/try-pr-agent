class Robot:
    def __init__(self):
        self._pos = [0, 0]
        self._vel = [0, 0]
        self._acc = [0, 0]
        self._yaw = 0

    def print(self):
        print(f"pos={self._pos}, vel={self._vel}, acc={self._acc}, yaw={self._yaw}")


if __name__ == "__main__":
    robot = Robot()
    robot.print()
