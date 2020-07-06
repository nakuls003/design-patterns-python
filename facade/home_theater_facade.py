from facade.home_theater_subsystem import PopcornPopper, TheaterLights, \
    DvdPlayer, Screen, Projector, Amplifier


class HomeTheaterFacade:
    def __init__(self, popper, lights, dvd_player, screen, projector, amplifier):
        self.popper = popper
        self.lights = lights
        self.dvd_player = dvd_player
        self.screen = screen
        self.projector = projector
        self.amplifier = amplifier

    def watch_movie(self, title):
        print('Starting movie: {}'.format(title))
        self.popper.on()
        self.popper.pop()
        self.lights.on()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.setDvd(self.dvd_player)
        self.projector.setWideScreenMode()
        self.amplifier.on()
        self.amplifier.setDvd(self.dvd_player)
        self.amplifier.setVolume(5)
        self.amplifier.setSurroundSound()
        self.dvd_player.on()
        self.dvd_player.play(title)

    def end_movie(self):
        print('Ending movie')
        self.popper.off()
        self.screen.up()
        self.projector.off()
        self.amplifier.off()
        self.dvd_player.stop()
        self.dvd_player.eject()
        self.dvd_player.off()
        self.lights.off()


if __name__ == '__main__':
    ht = HomeTheaterFacade(PopcornPopper(), TheaterLights(), DvdPlayer(), Screen(), Projector(),
                           Amplifier())
    ht.watch_movie('Rambo, first blood')
    ht.end_movie()
