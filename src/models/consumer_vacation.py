class ConsumerVacation:
    def __init__(self, weekNumber, consumer):
        self.weekNumber = weekNumber
        self.consumer = consumer

    def __repr__(self):
        return str(self.weekNumber) + ' -> ' + self.consumer

