from collections import defaultdict

from src.models.consumer_vacation import ConsumerVacation

class MasterChef:
    def __init__(self, consumersToProcess, consumersVacations):
        self.consumersToProcess = consumersToProcess
        self.consumersVacations = consumersVacations

        self.consumersVacationsList = []
        self.groupedConsumersVacations = defaultdict(list)

        self.prepareConsumersVacationsList()
        self.prepareGroupedVacationsForConsumers()

    def prepareConsumersVacationsList(self):
        for row in self.consumersVacations:
            weekNumber = row[0]
            for consumer in row[1:]:
                self.consumersVacationsList.append(ConsumerVacation(weekNumber, consumer))

    def prepareGroupedVacationsForConsumers(self):
        for consumerVacation in self.consumersVacationsList:
            self.groupedConsumersVacations[consumerVacation.weekNumber].append(consumerVacation.consumer)

    def getFirstAvailableMenuForConsumersForWeek(self, fullWeekIdentifier):
        if fullWeekIdentifier is None:
            raise RuntimeError("'CurrentWeek' parameter not provided or 'None'.")

        weekIdentifiers = fullWeekIdentifier.split("/")

        availablesMenuForConsumers = []
        nextWeekStartSearch = int(weekIdentifiers[1]) + 1

        for consumer in self.consumersToProcess:
            for week in range(nextWeekStartSearch, 53):
                if consumer not in self.groupedConsumersVacations[fullWeekIdentifier]:
                    fullWeekIdentifier =  str(weekIdentifiers[0]) + "/" + str(week)
                    availablesMenuForConsumers.append({
                            "consumer": consumer,
                            "menu": fullWeekIdentifier
                        })

                    break

        return availablesMenuForConsumers


