class Vars:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.CURRENT_STEP = 1
            self.TIME_STEPS = 100

            # Autocorrelation value (1 means always the same as previous, 0 means completely random)
            self.AUTOCORRELATION = 0.1

            self.initialized = True

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
