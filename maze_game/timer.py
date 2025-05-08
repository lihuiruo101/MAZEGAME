import time

class Timer:
    def __init__(self, duration):
        self.duration = duration
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def time_left(self):
        elapsed = time.time() - self.start_time
        return max(0, self.duration - elapsed)

    def time_taken(self):
        return time.time() - self.start_time

    def is_time_up(self):
        return self.time_left() <= 0
