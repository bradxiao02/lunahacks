import datetime

class SleepTracker:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start_sleep(self):
        self.start_time = datetime.datetime.now()

    def end_sleep(self):
        self.end_time = datetime.datetime.now()

    def get_sleep_duration(self):
        if self.start_time is not None and self.end_time is not None:
            duration = self.end_time - self.start_time
            return duration.total_seconds() / 3600
        else:
            return None

if __name__ == "__main__":
    tracker = SleepTracker()
    tracker.start_sleep()
    # Sleep for some time
    tracker.end_sleep()
    duration = tracker.get_sleep_duration()
    if duration is not None:
        print("You slept for {:.2f} hours.".format(duration))
    else:
        print("You haven't slept yet.")

