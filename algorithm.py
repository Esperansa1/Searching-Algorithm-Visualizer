
class Algorithm:
    def __init__(self, name) -> None:
        self.name = name
        self.run_simulation = False
        self.start_point = None
        self.end_point = None
        self.grid = []
