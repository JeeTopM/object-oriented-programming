class Time:
    @staticmethod
    def count_time(distance, speed):
        time = distance / speed
        return time
print(Time.count_time(500, 100))