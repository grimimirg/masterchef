import unittest

from datetime import datetime, timedelta

from src.procedures.masterchef import MasterChef

class TestMasterChefTest(unittest.TestCase):

    def test_getFirstAvailableConsumersMenuForWeek_shouldThrowException_whenNullArgumentIsProvided(self):
        # GIVEN
        masterChef = MasterChef([], [])
        
        # WHEN
        with self.assertRaises(RuntimeError) as context:
            masterChef.getFirstAvailableMenuForConsumersForWeek(None)

        # THEN
        self.assertEqual(str(context.exception), "'CurrentWeek' parameter not provided or 'None'.")


    def test_getFirstAvailableConsumersMenuForWeek_shouldReturnEmptySet_whenConsumersToProceedInConsumersVacations(self):
        # GIVEN
        nowIsoDate1 = datetime.now().isocalendar()
        nowIsoDate2 = (datetime.now() + timedelta(days=7)).isocalendar()

        week1 = str(nowIsoDate1[0]) + "/" + str(nowIsoDate1[1])
        week2 = str(nowIsoDate2[0]) + "/" + str(nowIsoDate2[1])

        consumersToProcess = ["L", "Z"]
        consumersVacations = [
                [week1, "Z", "L", "A"],
                [week2, "L", "Z"]
            ]

        masterChef = MasterChef(consumersToProcess, consumersVacations)

        # WHEN
        availableMenuForConsumers = masterChef.getFirstAvailableMenuForConsumersForWeek(week1)

        # THEN
        self.assertEqual(availableMenuForConsumers, [])
 

    def test_getFirstAvailableConsumersMenuForWeek_shouldReturnConsumers_withFirstAvailableMenu(self):
        # GIVEN
        nowIsoDate1 = datetime.now().isocalendar()
        nowIsoDate2 = (datetime.now() + timedelta(days=7)).isocalendar()

        week1 = str(nowIsoDate1[0]) + "/" + str(nowIsoDate1[1])
        week2 = str(nowIsoDate2[0]) + "/" + str(nowIsoDate2[1])

        consumersToProcess = ["K", "C"]
        consumersAvailabilities = [
                [week1, "A", "G", "F"],
                [week2, "N", "O"]
            ]

        masterChef = MasterChef(consumersToProcess, consumersAvailabilities)

        # WHEN
        availableMenuForConsumers = masterChef.getFirstAvailableMenuForConsumersForWeek(week1)

        # THEN
        self.assertEqual(
                availableMenuForConsumers, [
                    {
                        "consumer": "K",
                        "menu": week2
                    },
                    {
                        "consumer": "C",
                        "menu": week2
                    }
                ])


if __name__ == "__main__":
    unittest.main()
