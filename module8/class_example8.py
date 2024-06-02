# class MarathonRunner:
#     race_distance = 42.195  # Marathon distance in Kilometers

#     def __init__(self):
#         return None

#     def get_speed(self):
#         return None

# runner1 = MarathonRunner()
# runner2 = MarathonRunner()

# print(MarathonRunner.race_distance)  # Look in class namespace
# print(runner1.race_distance)  # Look in instance namespace
# print(runner2.race_distance)


class MarathonRunner:
    race_distance = 42.195  # Marathon distance in Kilometers

    def __init__(self):
        self.speed = 0
        return None

    def get_speed(self):
        return None

runner1 = MarathonRunner()
runner1.speed = 7.5

runner2 = MarathonRunner()
runner2.speed = 8.0

print('Runner 1 speed:', runner1.speed)
print('Runner 2 speed:', runner2.speed)

