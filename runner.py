from custom_errors import *
import re
import csv
import warnings
warnings.filterwarnings('ignore')
import pandas as pd

class Runner:
    # max_energy = 1000
    def __init__(self, name, age, country, sprint_speed, endurance_speed):
        self.max_energy = 1000
        self.name = name
        self.age = age
        self.country = country
        self.sprint_speed = sprint_speed
        self.endurance_speed = endurance_speed
        self.energy = self.max_energy
        
        if not all(char.isalnum() or char.isspace() for char in self.name):
            # raise CustomValueError 
            raise CustomTypeError("Name must be an alphanumeric string and can contain spaces.")
        
        if not isinstance(self.age, int) or not (5 <= self.age <= 120):
            # raise Exception
            raise CustomTypeError("Age must be an integer between 5 and 120.")
        
        if not isinstance(self.country, str):
            # raise Exception
            raise CustomValueError("Country must be a string and its value must be in the provided countries list.")
        
        with open("countries.csv") as file:
            data = pd.read_csv(file)
        if self.country.lower() not in list(data['name'].str.lower()):
            # raise Exception
            raise CustomValueError("Country must be a string and its value must be in the provided countries list.")
        
        if not isinstance(self.sprint_speed, float) or not (2.2 <= self.sprint_speed <= 6.8):
            # raise Exception
            raise CustomTypeError("Sprint speed must be a float between 2.2 and 6.8 meters per second.")
        
        if not isinstance(self.endurance_speed, float) or not (1.8 <= self.endurance_speed <= 5.4):
            # raise Exception
            raise CustomValueError("Endurance speed must be a float between 1.8 and 5.4 meters per second.")

    def drain_energy(self, drain_points):
        # self.energy -= drain_points
        if not isinstance(drain_points, int) :
            raise CustomTypeError("Drain points must be a non-negative integer.")
        if drain_points < 0:
            raise CustomValueError("Drain points must be a non-negative integer.")
        if drain_points > self.max_energy:
            raise CustomValueError("Drain points cannot exceed the max energy value.")
        if self.energy - drain_points < 0:
            raise CustomValueError("Energy cannot be less than 0 after draining.")

        self.energy -= drain_points
        return self.energy
    
    def recover_energy(self, recovery_amount):
        if not isinstance(recovery_amount, int) or recovery_amount < 0:
            raise CustomTypeError("Recovery amount must be a non-negative integer.")
        if recovery_amount > self.max_energy:
            raise CustomValueError("Recovery amount cannot exceed the max energy value.")

        self.energy += recovery_amount
        if self.energy > self.max_energy:
            self.energy = self.max_energy
        # self.energy += recovery_amount
        return self.energy
    
    def run_race(self, race_type, distance):
        distance=distance*1000
        if race_type not in ['short', 'long']:
            raise CustomValueError("Race type must be either 'short' or 'long'.")
        if not isinstance(distance, (float)) :
            raise CustomTypeError("Distance must be a positive number.")
        if distance <= 0:
            raise CustomValueError("Distance must be a positive number.")

        if race_type == 'short':
            speed = self.sprint_speed
        else:
            speed = self.endurance_speed

        time_taken = distance / speed  # distance is in km, speed in m/s, convert km to m
        return round(time_taken, 2)
        # race_type = 'short'
        # return distance * self.sprint_speed
    
    def __str__(self):
        return f"Name: {self.name} Age: {self.age} Country: {self.country}"
   
if __name__ == '__main__':
    runner = Runner('Elij111 ah', 8, 'Australia', 5.8, 4.4)
    
    # running a short race
    time_taken = runner.run_race('short', 2.0)
    print(f"Runner {runner.name} took {time_taken} seconds to run 2km!")
    print(runner)

    print(runner.energy)
    # runner.drain_energy(400)
    print(runner.energy)