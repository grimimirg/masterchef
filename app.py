from collections import defaultdict

#
#--------------------------------------------------
# DATA
#

consumers = ["A", "B", "C", "D", "E"]

consumersCalendar = [
    [1, 'A', 'B', 'C', 'D', 'E'],
    [2, 'A', '/', 'C', '/', 'E'],
    [3, 'A', '/', '/', '/', '/'],
    [4, '/', '/', '/', '/', '/'],
    [5, '/', '/', '/', '/', '/'],
    [6, 'A', '/', '/', '/', '/'],
    [7, 'A', 'B', '/', '/', '/'],
    [8, 'A', 'B', 'C', '/', '/'],
    [9, '/', 'B', 'C', '/', '/'],
    [10, '/', 'B', 'C', 'D', '/'],
    [11, '/', 'B', 'C', 'D', '/'],
    [12, '/', 'B', 'C', 'D', 'E'],
    [13, '/', '/', '/', '/', '/'],
    [14, '/', '/', '/', '/', '/'],
    [15, '/', '/', 'C', 'D', 'E'],
    [16, 'A', 'B', '/', '/', '/'],
    [17, '/', 'B', '/', '/', '/'],
    [18, '/', 'B', '/', '/', '/'],
    [19, 'A', 'B', '/', '/', '/'],
    [20, 'A', '/', '/', 'D', 'E'],
    [21, '/', '/', '/', '/', '/'],
    [22, 'A', '/', '/', '/', '/'],
    [23, '/', '/', '/', 'D', '/'],
    [24, '/', '/', '/', '/', 'E'],
    [25, 'A', '/', 'C', '/', '/'],
    [26, 'A', 'B', '/', '/', '/'],
    [27, 'A', 'B', '/', 'D', 'E'],
    [28, '/', 'B', '/', 'D', '/'],
    [29, '/', 'B', 'C', 'D', '/'],
    [30, 'A', 'B', '/', 'D', '/'],
    [31, 'A', 'B', 'C', '/', 'E'],
    [32, 'A', 'B', '/', '/', '/'],
    [33, '/', 'B', '/', 'D', '/'],
    [34, 'A', '/', 'C', 'D', '/'],
    [35, '/', '/', 'C', '/', 'E'],
    [36, 'A', '/', 'C', 'D', 'E'],
    [37, 'A', '/', '/', '/', '/'],
    [38, 'A', '/', '/', '/', '/'],
    [39, '/', '/', '/', 'D', '/'],
    [40, '/', '/', 'C', '/', 'E'],
    [41, '/', '/', 'C', '/', '/'],
    [42, 'A', '/', 'C', '/', '/'],
    [43, 'A', '/', '/', '/', '/'],
    [44, 'A', 'B', '/', 'D', '/'],
    [45, '/', 'B', '/', 'D', '/'],
    [46, 'A', 'B', '/', 'D', '/'],
    [47, '/', 'B', '/', '/', '/'],
    [48, 'A', '/', 'C', 'D', '/'],
    [49, 'A', 'B', '/', '/', '/'],
    [50, '/', 'B', '/', '/', '/'],
    [51, '/', '/', '/', '/', '/'],
    [52, 'A', 'B', 'C', 'D', 'E']
]

lastReceivedMenuesForConsumers = ["A-0", "B-0", "C-0", "D-0", "E-0"]

#
#--------------------------------------------------
# CLASSES
#

class ConsumerAvailability:
    def __init__(self, weekNumber, consumer):
        self.weekNumber = weekNumber
        self.consumer = consumer

    def __repr__(self):
        return str(self.weekNumber) + ' -> ' + self.consumer

#--------------------------------------------------

class MasterChef:
    def __init__(self, data):
        self.data = data
        self.consumersAvailabilities = []
        self.groupedConsumersAvailabilities = defaultdict(list)

        self.prepareData()
        self.prepareGroupedDataForConsumers()

    def prepareData(self):
        for row in self.data:
            weekNumber = row[0]
            for consumer in row[1:]:
                if consumer != "/":
                    self.consumersAvailabilities.append(ConsumerAvailability(weekNumber, consumer))

    def getConsumersAvailabilities(self):
        return self.consumersAvailabilities

    def prepareGroupedDataForConsumers(self):
        for consumerAvailability in self.consumersAvailabilities:
            self.groupedConsumersAvailabilities[consumerAvailability.consumer].append(consumerAvailability.weekNumber)

    def addAvailability(self, weekNumber, consumer):
        consumerAvailability = ConsumerAvailability(weekNumber, consumer)

        self.consumersAvailabilities.append(consumerAvailability)
        self.groupedConsumerAvailabilities[consumer].append(weekNumber)

    def removeAvailability(self, weekNumber, consumer):
        consumerAvailabilityToRemove = None
        for availability in self.consumersAvailabilities:
            if availability.weekNumber == weekNumber and availability.consumer == consumer:
                consumerAvailabilityToRemove = availability
                break
        
        if consumerAvailabilityToRemove:
            self.consumersAvailabilities.remove(consumerAvailabilityToRemove)
            self.groupedConsumersAvailabilities[consumer].remove(weekNumber)
            if not self.groupedConsumersAvailabilities[consumer]:
                del self.groupedConsumersAvailabilities[consumer]

    def getFirstAvailableWeekForConsumer(self, consumer):
        return min(self.groupedConsumersAvailabilities[consumer]) if consumer in self.groupedConsumersAvailabilities else None


#
#--------------------------------------------------
# MAIN
#

def main():
    masterchef = MasterChef(consumersCalendar)

    for week in range(52):
        for consumer in consumers:
            print("*******************************")
            print(f"WEEK: {week}")
            print("*******************************")
            
            foundConsumers = [item for item in lastReceivedMenuesForConsumers if item == (consumer + '-' + str(week))]

            if foundConsumers:
                print(f"First available week for consumer {consumer}")
                firstAvailableWeekForConsumer = masterchef.getFirstAvailableWeekForConsumer(consumer)
                print(f"{firstAvailableWeekForConsumer}")

                print(f"REFERENCES: {lastReceivedMenuesForConsumers}")
                print(f"Removing old reference {foundConsumers[0]}...")
                lastReceivedMenuesForConsumers.remove(foundConsumers[0])

                print(f"Sending menu to {consumer} for week {str(firstAvailableWeekForConsumer)}....")

                print(f"Removing {str(week)} for {consumer} from availabilities...")
                masterchef.removeAvailability(firstAvailableWeekForConsumer, consumer)
                
                print(f"Adding new reference for {consumer} on week {str(firstAvailableWeekForConsumer)}...")
                lastReceivedMenuesForConsumers.append(consumer + "-" + str(firstAvailableWeekForConsumer))
            else:
                print(f"Nothing for {consumer} on week {str(week)}")
    

if __name__ == '__main__':
    main()
    
