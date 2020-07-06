class PopcornPopper:
    def on(self):
        print("Popcorn Popper is on")

    def off(self):
        print("Popcorn Popper is off")

    def pop(self):
        print('Popping delicious popcorn for you')


class TheaterLights:
    def on(self):
        print('Turning theater lights on')

    def off(self):
        print('Turning theater lights off')

    def dim(self, val):
        print("Dimming theater lights to {}%".format(val))


class Screen:
    def up(self):
        print('Pulling screen up')

    def down(self):
        print('Pulling screen down')


class DvdPlayer:
    def on(self):
        print('Turning Dvd player on')

    def off(self):
        print('Turning Dvd player off')

    def play(self, movie):
        print('Playing movie {}'.format(movie))

    def pause(self):
        print('Pausing movie')

    def stop(self):
        print('Stopping movie')

    def eject(self):
        print('Ejecting Dvd from Dvd player')


class Amplifier:
    def on(self):
        print('Turning Amplifier on')

    def off(self):
        print('Turning Amplifier off')

    def setDvd(self, dvd):
        print('Connecting amplifier to Dvd output')

    def setSurroundSound(self):
        print('Setting amplifier to surround sound mode: 5 speakers, 1 subwoofer')

    def setVolume(self, val):
        print('Setting amplifier volume to {}'.format(val))


class Projector:
    def on(self):
        print('Turning Projector on')

    def off(self):
        print('Turning Projector off')

    def setDvd(self, dvd):
        print('Connecting projector output to Dvd')

    def setWideScreenMode(self):
        print('Changing projector mode to wide screen display, aspect ratio 16x9')

