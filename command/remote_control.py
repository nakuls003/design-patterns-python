from command.appliances import Light, GarageDoor, Stereo
from command.commands import NoCommand, LightOnCommand, LightOffCommand, GarageDoorUpCommand, GarageDoorDownCommand, \
    StereoOnCommand, StereoOffCommand, CeilingFan, CeilingFanHighCommand, CeilingFanLowCommand, CeilingFanOffCommand, \
    LightDimCommand, MacroCommand


class RemoteControl:
    def __init__(self):
        self.on_commands = [NoCommand()]*7
        self.off_commands = [NoCommand()]*7
        self.prev_command = NoCommand()

    def set_slot(self, slot, on_command, off_command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_pressed(self, slot):
        self.on_commands[slot].execute()
        self.prev_command = self.on_commands[slot]

    def off_button_pressed(self, slot):
        self.off_commands[slot].execute()
        self.prev_command = self.off_commands[slot]

    def undo_button_pressed(self):
        self.prev_command.undo()

    def __str__(self):
        ans = []
        for i in range(7):
            ans.append('Slot {}: {} {}'.format(i, self.on_commands[i].__class__.__name__,
                                          self.off_commands[i].__class__.__name__))
        return '\n'.join(ans)


if __name__ == '__main__':
    remote = RemoteControl()

    kitchen_light = Light('Kitchen Light')
    living_room_light = Light('Living Room Light')
    garage_door = GarageDoor('Garage Door')
    stereo = Stereo('Living Room Stereo')
    ceiling_fan = CeilingFan('Bedroom ceiling fan')

    kitchen_light_on_command = LightOnCommand(kitchen_light)
    kitchen_light_off_command = LightOffCommand(kitchen_light)

    living_room_light_on_command = LightOnCommand(living_room_light)
    living_room_light_off_command = LightOffCommand(living_room_light)
    living_room_light_dim_command = LightDimCommand(living_room_light)

    garage_door_up_command = GarageDoorUpCommand(garage_door)
    garage_door_down_command = GarageDoorDownCommand(garage_door)

    stereo_on_command = StereoOnCommand(stereo)
    stereo_off_command = StereoOffCommand(stereo)

    ceiling_fan_high_command = CeilingFanHighCommand(ceiling_fan)
    ceiling_fan_low_command = CeilingFanLowCommand(ceiling_fan)
    ceiling_fan_off_command = CeilingFanOffCommand(ceiling_fan)

    party_mode_on_command = MacroCommand([living_room_light_dim_command, stereo_on_command])
    party_mode_off_command = MacroCommand([living_room_light_off_command, stereo_off_command])

    remote.set_slot(0, kitchen_light_on_command, kitchen_light_off_command)
    remote.set_slot(1, living_room_light_on_command, living_room_light_off_command)
    remote.set_slot(2, garage_door_up_command, garage_door_down_command)
    remote.set_slot(3, stereo_on_command, stereo_off_command)
    remote.set_slot(4, ceiling_fan_high_command, ceiling_fan_off_command)
    remote.set_slot(5, ceiling_fan_low_command, ceiling_fan_off_command)
    remote.set_slot(6, party_mode_on_command, party_mode_off_command)

    print(remote)

    remote.on_button_pressed(0)
    remote.off_button_pressed(0)
    print()
    remote.on_button_pressed(1)
    remote.off_button_pressed(1)
    remote.on_button_pressed(1)
    print()
    remote.on_button_pressed(2)
    remote.off_button_pressed(2)
    remote.undo_button_pressed()
    print()
    remote.on_button_pressed(3)
    remote.off_button_pressed(3)
    remote.undo_button_pressed()
    print()
    remote.on_button_pressed(4)
    remote.on_button_pressed(5)
    remote.undo_button_pressed()
    remote.off_button_pressed(5)
    print()
    remote.on_button_pressed(6)
    remote.undo_button_pressed()
    remote.off_button_pressed(6)
