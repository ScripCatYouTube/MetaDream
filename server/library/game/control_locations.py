from .location import Location


class ControlLocations:
    def __init__(self) -> None:
        self.locations = {}


    def add_location(self, location: Location, name: str = 'location') -> None:
        self.locations[name] = location


    def get_location(self, name: str = 'location') -> Location:
        try:
            return self.locations[name]

        except KeyError: return