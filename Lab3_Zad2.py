# Stanisław Kusiak

import json
import os

class Person:
    def __init__(self, first_name, second_name, phone_number):
        self.first_name = first_name
        self.second_name = second_name
        self.phone_number = phone_number

    def save_to_json(self):
        dictionary = {
            "first_name": self.first_name,
            "second_name": self.second_name,
            "phone_number": self.phone_number
        }
        file_name = "person_log.json"
        json_obj = json.dumps(dictionary, indent=4)
        with open(file_name, "w") as output:
            output.write(json_obj)

    def read_from_json(self):
        file_name = "person_log.json"
        with open(file_name, "r") as input:
            json_obj = json.load(input)
            self.first_name = json_obj['first_name']
            self.second_name = json_obj['second_name']
            self.phone_number = json_obj['phone_number']

p1 = Person("Jan", "Kowalski", 123456789)
p1.save_to_json()

p2 = Person("a", "b", "0")
p2.read_from_json()
print(p2.first_name, p2.second_name, p2.phone_number)