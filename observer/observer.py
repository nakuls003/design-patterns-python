from abc import ABC, abstractmethod
import uuid


class Observable(ABC):
    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class WeatherData(Observable):
    def __init__(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.observers = {}

    def add_observer(self, observer):
        self.observers[observer.id] = observer

    def remove_observer(self, observer):
        if observer.id in self.observers:
            del self.observers[observer.id]

    def notify(self):
        for observer in self.observers.values():
            observer.update()

    def update_measurements(self):
        self.notify()

    def set_weather_data(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.update_measurements()


class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass


class CurrentWeatherDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self.id = uuid.uuid4().hex
        self.temperature = None
        self.humidity = None
        self.weather_data = weather_data
        self.weather_data.add_observer(self)

    def remove_as_observer(self):
        self.weather_data.remove_observer(self)

    def update(self):
        self.temperature = self.weather_data.temperature
        self.humidity = self.weather_data.humidity
        self.display()

    def display(self):
        print("Temperature is {}, humidity is {}".format(self.temperature, self.humidity))


class AtmosphericPressureDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self.id = uuid.uuid4().hex
        self.pressure = None
        self.weather_data = weather_data
        self.weather_data.add_observer(self)

    def remove_as_observer(self):
        self.weather_data.remove_observer(self)

    def update(self):
        self.pressure = self.weather_data.pressure
        self.display()

    def display(self):
        print("Atmospheric Pressure is {}".format(self.pressure))


if __name__ == '__main__':
    wd = WeatherData(0, 0, 0)
    current_weather_display = CurrentWeatherDisplay(wd)
    atmospheric_pressure_display = AtmosphericPressureDisplay(wd)

    dummy_sensor_data = [(34, 89, 50), (26, 60, 53), (9, 62, 45)]
    for temp, humidity, pressure in dummy_sensor_data:
        wd.set_weather_data(temp, humidity, pressure)
