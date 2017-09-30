
from random import randint

class Die:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

A = Die(6)
A.roll_die()
A.roll_die()
A.roll_die()
A.roll_die()
A.roll_die()
A.roll_die()
A.roll_die()
A.roll_die()
A.roll_die()
A.roll_die()

B = Die(10)
B.roll_die()
B.roll_die()
B.roll_die()
B.roll_die()
B.roll_die()
B.roll_die()
B.roll_die()
B.roll_die()
B.roll_die()
B.roll_die()

C = Die(20)
C.roll_die()
C.roll_die()
C.roll_die()
C.roll_die()
C.roll_die()
C.roll_die()
C.roll_die()
C.roll_die()
C.roll_die()
C.roll_die()
