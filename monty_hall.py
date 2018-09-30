''' This module tests the answer(Answer of marilyn vos savant)
to the famous monty hall problem.
'''

import sys
import random


class MontyHall:
    '''
    This class contains all components of the problem.
    '''

    def set_doors(self):
        '''
        Set the goat or the car behind the doors randomly.
        '''
        self.car_index = random.randint(0, 2)
        self.doors = ['car' if index == self.car_index else 'goat' for index in range(0, 3)]

    def select_door(self):
        '''
        Function to randomly select a door.
        '''
        self.selected_door = random.randint(0, 2)

    def select_door_with_goat(self):
        '''
        Host decides to select a door and tell the player that
        there is a goat behind it.
        '''
        for index in range(0, 3):
            # Door should not have car behind it nor it should be
            # one selected by the guest.
            if index != self.car_index and index != self.selected_door:
                self.exposed_index = index
                break

    def switch_door(self):
        '''
        Switch the door initially selected by the guest
        '''
        # User changes the initial decision
        for index in range(0, 3):
            # Switch door
            if index != self.selected_door and index != self.exposed_index:
                self.new_selected_door = index
                break

    def test_result(self):
        '''
        Output of the experiment.
        '''
        self.set_doors()
        self.select_door()
        self.select_door_with_goat()
        # We test the number of times the users decision to switch door
        # is correct
        self.switch_door()
        return self.car_index == self.new_selected_door

if __name__ == '__main__':

    # Create a one time simulation object for testing purpose
    monty_hall = MontyHall()

    # Take input from the user for number of tests to be performed.
    test_cases = int(input('Test Cases: '))
    success_guess_count = 0
    for test_case in range(test_cases):
        success_guess_count += int(monty_hall.test_result())

    # Calculate the percentage of successful switches
    percent_success = (success_guess_count / test_cases) * 100

    # Display the output
    print("Total test cases: {}".format(str(test_cases)))
    print("Success after switching the door: {}".format(str(success_guess_count)))
    print("Success in percentage: {}".format(str(percent_success)))
