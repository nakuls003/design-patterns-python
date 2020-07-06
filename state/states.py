from abc import ABC, abstractmethod
import random

class State:

    @abstractmethod
    def insert_quarter(self):
        pass

    @abstractmethod
    def eject_quarter(self):
        pass

    @abstractmethod
    def turn_crank(self):
        pass

    @abstractmethod
    def dispense(self):
        pass

    @abstractmethod
    def refill(self, count):
        pass


class NoQuarterState(State):

    def __init__(self, machine):
        self.machine = machine

    def insert_quarter(self):
        print("Inserted a quarter")
        self.machine.state = self.machine.HAS_QUARTER_STATE

    def eject_quarter(self):
        print("You didn't insert a quarter, can't eject")

    def turn_crank(self):
        print("Please insert a quarter first")

    def dispense(self):
        print("Please insert a quarter first")

    def refill(self, count):
        print("Can't refill if the machine isn't empty")


class HasQuarterState(State):

    def __init__(self, machine):
        self.machine = machine

    def insert_quarter(self):
        print("You've already inserted a quarter")

    def eject_quarter(self):
        print("Returning your quarter")
        self.machine.state = self.machine.NO_QUARTER_STATE

    def turn_crank(self):
        print("You turned...")
        val = random.randint(1, 10)
        if val == 5:
            self.machine.state = self.machine.WINNER_STATE
        else:
            self.machine.state = self.machine.SOLD_STATE

    def dispense(self):
        print("Please turn the crank first")

    def refill(self, count):
        print("Can't refill if the machine isn't empty")


class SoldState(State):

    def __init__(self, machine):
        self.machine = machine

    def insert_quarter(self):
        print("You already getting a gumball, hang on")

    def eject_quarter(self):
        print("You already turned the crank, can't return quarter now")

    def turn_crank(self):
        print("Turning crank twice won't get you more gumballs")

    def dispense(self):
        print('Here comes your gumball rolling out of the slot')
        self.machine.release_ball()
        if self.machine.count == 0:
            self.machine.state = self.machine.SOLD_OUT_STATE
        else:
            self.machine.state = self.machine.NO_QUARTER_STATE

    def refill(self, count):
        print("Can't refill if the machine isn't empty")


class WinnerState(State):

    def __init__(self, machine):
        self.machine = machine

    def insert_quarter(self):
        print("You already getting a gumball, hang on")

    def eject_quarter(self):
        print("You already turned the crank, can't return quarter now")

    def turn_crank(self):
        print("Turning crank twice won't get you more gumballs")

    def dispense(self):
        print('Lucky winner! You get two gumballs')
        self.machine.release_ball()
        if self.machine.count > 0:
            self.machine.release_ball()
            if self.machine.count == 0:
                self.machine.state = self.machine.SOLD_OUT_STATE
            else:
                self.machine.state = self.machine.NO_QUARTER_STATE
        else:
            self.machine.state = self.machine.SOLD_OUT_STATE

    def refill(self, count):
        print("Can't refill if the machine isn't empty")


class SoldOutState(State):

    def __init__(self, machine):
        self.machine = machine

    def insert_quarter(self):
        print("No gumballs left, we're sold out")

    def eject_quarter(self):
        print("No gumballs left, we're sold out")

    def turn_crank(self):
        print("No gumballs left, we're sold out")

    def dispense(self):
        print("No gumballs left, we're sold out")

    def refill(self, count):
        print("Refilling the machine")
        self.machine.count = count
        self.machine.state = self.machine.NO_QUARTER_STATE
