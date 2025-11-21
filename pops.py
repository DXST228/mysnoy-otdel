from random import randint
from const import qs

class Pops:
    def __init__(self, questions=qs):
        self.qs = questions
        self.initquestions = questions
        self.numbers = len(self.qs)
        self.now =randint(0,len(self.qs)-1)
        self.answered = 1
        self.trueanswerd = 0
    def next(self):
        if self.answered < self.numbers:
            self.qs.remove(self.qs[self.now])
            self.now =randint(0,len(self.qs)-1)
            self.answered+=1
        else:
            self.qs = self.initquestions
            self.answered = 1
            self.trueanswerd = 0   
    def levelup(self):
        if self.trueanswerd < self.numbers:
            self.trueanswerd+=1
        else:
            self.trueanswerd =0