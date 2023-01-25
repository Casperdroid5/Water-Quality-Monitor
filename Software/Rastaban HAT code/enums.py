from enum import Enum, unique


class State(Enum):

    OFF = 0
    ON = 1
    HOT = 2
    COLD = 3
    CUSTOM = 4
    MOTOR_ENABLED = 5
    MOTOR_DISABLED = 6
    MOTOR_CLOCKWISE = 7
    MOTOR_COUNTERCLOCKWISE = 8
    STEP = 9
    ENABLE = 10
    PHASE = 11
    SLEEP = 12
