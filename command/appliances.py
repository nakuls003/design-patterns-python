class Light:
    ON = 2
    DIM = 1
    OFF = 0

    def __init__(self, description):
        self.description = description
        self.state = self.OFF

    def on(self):
        print('Light is on')
        self.state = self.ON

    def off(self):
        print('Light is off')
        self.state = self.OFF

    def dim(self):
        print('Light is dimmed')
        self.state = self.DIM


class GarageDoor:
    def __init__(self, description):
        self.description = description

    def up(self):
        print('Garage door is up')

    def down(self):
        print('Garage door is down')

    def stop(self):
        print('Garage door is stopped')


class Stereo:
    def __init__(self, description):
        self.description = description

    def on(self):
        print('Stereo is on')

    def setCD(self):
        print('Setting CD in Stereo')

    def setVolume(self, value):
        print('Setting volume to {}'.format(value))

    def off(self):
        print('Stereo is off')


class CeilingFan:
    OFF = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    def __init__(self, description):
        self.description = description
        self.speed = self.OFF

    def high(self):
        print('turning fan on to high')
        self.speed = self.HIGH

    def medium(self):
        print('turning fan on to medium')
        self.speed = self.MEDIUM

    def low(self):
        print('turning fan on to low')
        self.speed = self.LOW

    def off(self):
        print('turning fan off')
        self.speed = self.OFF
