import random

class Wallet:
    def __init__(self,  identification, current_value=0):
        self.current_value = current_value
        self.identification = identification

    def send(self, target):
        amount = round(random.uniform(0, self.current_value*0.05), random.randint(0,5))
        self.current_value -= amount
        target.receive(amount)

    def receive(self, amount):
        self.current_value += amount

    def get_current_value(self):
        return self.current_value

    def set_current_value(self, value):
        self.current_value = value

    def get_identification(self):
        return self.identification
