class Time:
#     """ A class that represents a time of day """
    def __init__(self):
        self.hours = 0
        self.minutes = 0
    def print_time(self, gmt):
        if gmt:
            print('Time is: {}:{} GMT'
                .format(self.hours-8, self.minutes))
        else:
            print('Time is: {}:{}'
                .format(self.hours, self.minutes))

time1 = Time()
time1.hours = 7
time1.minutes = 15
time1.print_time(False)
time1.print_time(True)