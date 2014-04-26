import unittest
import greatcircle
import calculator
   
class DutchpostcodesTest(unittest.TestCase):

    def test_greatcircle(self):
        martinitoren = (53.219332, 6.568239) # the Martinitoren in Groningen
        csamsterdam = (52.378230, 4.899997) # Amsterdam Central Station
        km = greatcircle.distance(martinitoren[0], martinitoren[1], csamsterdam[0], csamsterdam[1])
        self.assertEqual(int(km), 146, "Distance between the Martinitoren and CS Amsterdam should be 146 km")

    def test_between(self):
        calc = calculator.Calculator()
        self.assertEqual(calc.distance(9718, 99999), None, "Distance between an existing and a non-existing postcode should be None")
        self.assertEqual(calc.distance(99999, 1000), None, "Distance between a non-existing and an existing postcode should be None")
        self.assertEqual(int(calc.distance(9718, 1000)), 146, "Distance between postcodes 9718 and 1000 should be 146 km")

    def test_within(self):
        calc = calculator.Calculator()
        within = [postcode for (postcode, km) in calc.postcodesaround(9718, 10)]
        self.assertEqual(len(within) > 0, True, "There should be al least one postcode within 10km of postcode 9718")
        self.assertEqual(9811 in within, True, "Postcode 9811 should be within 10km of postcode 9718")
        self.assertEqual(1200 in within, False, "Postcode 1200 shouldn't be within 10km of postcode 9718")
        
if __name__ == "__main__":
    unittest.main()
