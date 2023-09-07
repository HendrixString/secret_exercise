import unittest
from typing import List
from machine.machine import Machine

def create_machine():
    return Machine("Start") \
    .add("Start", "red", "R1") \
    .add("Start", "yellow", "Y1") \
    .add("R1", "red", "R2") \
    .add("R1", "yellow", "Y1") \
    .add("R2", "red", "R3") \
    .add("R2", "yellow", "Y1") \
    .add("R3", "red", "R4") \
    .add("R3", "yellow", "Y1") \
    .add("R4", "red", "R4") \
    .add("R4", "yellow", "Y1") \
    .add("Y1", "red", "R1") \
    .add("Y1", "yellow", "Y2") \
    .add("Y2", "red", "R1") \
    .add("Y2", "yellow", "Y3") \
    .add("Y3", "red", "R1") \
    .add("Y3", "yellow", "Y4") \
    .add("Y4", "red", "R1") \
    .add("Y4", "yellow", "Y4")

A = "red" # red event
B = "yellow" # yellow event

LINE_1 = [A, B, A, B, A, B, A, B, A]
LINE_2 = [A, B, A, A, B, A, B, A]
LINE_3 = [A, B, A, A, A]
LINE_4 = [A, B, A, A, A, A, A, B, B, B, B]

def iterate_factory_line(input: List[int], start_state=0):
    print(f'\nRuning: {input} ')

    for state in create_machine().iterate_input(input):
        if state=="R3":
            print('Oh No! Too many RED Lolipops :(')
        elif state=="Y3":
            print('Oh No! Too many Yellow Lolipops :(')
    
    print('Run finished.')

class TestSum(unittest.TestCase):

    def test_1(self):
        iterate_factory_line(LINE_1)

    def test_2(self):
        iterate_factory_line(LINE_2)

    def test_3(self):
        iterate_factory_line(LINE_3)

    def test_4(self):
        iterate_factory_line(LINE_4)
    
    def test_sanity(self):
        for state in create_machine().iterate_input(['red', 'yellow', 'red', 'yellow', 'red', 'yellow', 'red', 'yellow']):
            print(state)

if __name__ == '__main__':
    unittest.main()