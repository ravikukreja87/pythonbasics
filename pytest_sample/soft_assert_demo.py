#Soft assertion --> Even when assertion fails, test continues to next step

#Assertion / Hard Assertion --> Stops the test once assertion error is encountered
# softest - This package/module allows soft assertions
import softest
from softest import TestCase


class TestAssertions(TestCase):
    def test_add(self):
        first = 2
        second = 3
        result = first+second
        # assert result == 6 #Hard assertion. If I user assertion flow terminates here is failure
        self.soft_assert(self.assertEqual, result, 6)
        print('\nThis will be executed since this is a soft assert')

        first = 3
        second = 3
        result = first+second
        self.soft_assert(self.assertEqual, result, 6)
        print('Assertion passed')

        self.assert_all()
