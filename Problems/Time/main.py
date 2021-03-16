class Time:

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    # use appropriate decorator
    @classmethod
    def from_string(cls, time):
        hour, minute = time.split(":")
        return cls(hour, minute)