
class SeriesProvider:
    def __init__(self):
        self.series = []
        self.index = 0

    def get_next_value(self):
        if self.index >= len(self.series):
            raise Exception("Index out of range of test series")
        return self.series[self.index]

    def set_series(self, series):
        self.series = series

    def load_series_from_file(self, filepath):
        pass
