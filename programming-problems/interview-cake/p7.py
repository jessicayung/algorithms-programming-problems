class TempTracker:

    def __init__(self):

        # For mean
        self.temp_count = 0
        self.mean = None
        self.sum = 0.0

        # For max
        self.max = None

        # For min
        self.min = None

        # For mode
        self.mode = None
        self.occurrences = [0] * 111
        self.max_occurrences = 0

    def insert(self, temp):

        # Update mean
        self.temp_count += 1
        self.sum += temp
        self.mean = self.sum / self.temp_count

        # Update max and min
        if (self.max is None) or (temp > self.max):
            self.max = temp
        if (self.min is None) or (temp < self.min):
            self.min = temp

        # Update mode
        self.occurrences[temp] += 1
        if self.occurrences[temp] > self.max_occurrences:
            self.max_occurrences = self.occurrences[temp]
            self.mode = temp

    def get_max(self):
        return self.max

    def get_min(self):
        return self.min

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode