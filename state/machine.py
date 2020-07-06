from state.states import NoQuarterState, HasQuarterState, SoldState, SoldOutState, WinnerState


class GumballMachine:
    NO_QUARTER_STATE = None
    HAS_QUARTER_STATE = None
    SOLD_STATE = None
    SOLD_OUT_STATE = None
    WINNER_STATE = None

    def __init__(self, initial_count):
        self.NO_QUARTER_STATE = NoQuarterState(self)
        self.HAS_QUARTER_STATE = HasQuarterState(self)
        self.SOLD_STATE = SoldState(self)
        self.SOLD_OUT_STATE = SoldOutState(self)
        self.WINNER_STATE = WinnerState(self)
        self.count = initial_count

        if self.count > 0:
            self.state = self.NO_QUARTER_STATE
        else:
            self.state = self.SOLD_OUT_STATE

    def insert_quarter(self):
        self.state.insert_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank()
        self.state.dispense()

    def refill(self, count):
        self.state.refill(count)

    def release_ball(self):
        if self.count > 0:
            self.count -= 1

    def __str__(self):
        return "Current state: {}".format(self.state.__class__.__name__)


if __name__ == '__main__':
    machine = GumballMachine(3)
    print(machine)
    machine.insert_quarter()
    machine.turn_crank()
    print(machine)
    machine.refill(4)
    machine.eject_quarter()
    machine.insert_quarter()
    machine.turn_crank()
    print(machine)
    machine.turn_crank()
    print(machine)
    machine.insert_quarter()
    machine.eject_quarter()
    machine.insert_quarter()
    machine.turn_crank()
    print(machine)
    machine.refill(5)
    print(machine)
