from abc import ABC, abstractmethod

from command.appliances import CeilingFan, Light


class Command:

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class NoCommand(Command):
    def execute(self):
        pass

    def undo(self):
        pass


class LightCommand(Command):
    def __init__(self, light):
        self.light = light
        self.prev_state = Light.OFF

    def undo(self):
        if self.prev_state == Light.OFF:
            self.light.off()
        elif self.prev_state == Light.DIM:
            self.light.dim()
        elif self.prev_state == Light.ON:
            self.light.on()


class LightOnCommand(LightCommand):
    def execute(self):
        self.prev_state = self.light.state
        self.light.on()


class LightOffCommand(LightCommand):
    def execute(self):
        self.prev_state = self.light.state
        self.light.off()


class LightDimCommand(LightCommand):
    def execute(self):
        self.prev_state = self.light.state
        self.light.dim()


class GarageDoorUpCommand(Command):
    def __init__(self, garage_door):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.up()

    def undo(self):
        self.garage_door.down()


class GarageDoorDownCommand(Command):
    def __init__(self, garage_door):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.down()

    def undo(self):
        self.garage_door.up()


class StereoOnCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()
        self.stereo.setCD()
        self.stereo.setVolume(11)

    def undo(self):
        self.stereo.off()


class StereoOffCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.off()

    def undo(self):
        self.stereo.on()
        self.stereo.setCD()
        self.stereo.setVolume(11)


class CeilingFanCommand(Command):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan
        self.prev_speed = CeilingFan.OFF

    def undo(self):
        if self.prev_speed == CeilingFan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == CeilingFan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == CeilingFan.LOW:
            self.ceiling_fan.low()
        elif self.prev_speed == CeilingFan.OFF:
            self.ceiling_fan.off()


class CeilingFanHighCommand(CeilingFanCommand):
    def execute(self):
        self.prev_speed = self.ceiling_fan.speed
        self.ceiling_fan.high()


class CeilingFanMediumCommand(CeilingFanCommand):
    def execute(self):
        self.prev_speed = self.ceiling_fan.speed
        self.ceiling_fan.medium()


class CeilingFanLowCommand(CeilingFanCommand):
    def execute(self):
        self.prev_speed = self.ceiling_fan.speed
        self.ceiling_fan.low()


class CeilingFanOffCommand(CeilingFanCommand):
    def execute(self):
        self.prev_speed = self.ceiling_fan.speed
        self.ceiling_fan.off()


class MacroCommand(Command):
    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in self.commands:
            command.undo()
