# imports the abstractmethod from the ABC module
from abc import ABC, abstractmethod


class car(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ", amount)
    # this function is telling us to pass in an argument,but won't tell you how or what
    # kind of data it will be.

        @abstractmethod
        def payment(self, amount):
            pass


class CreditCardPayment(car):
    # Here we've defined how to implement the payment function from its parent paySlip class.
    def payment(self, amount):
        print(
            'Your purchase amount of {} exceeded your credit limit by 600$ '.format(amount))


obj = CreditCardPayment()
obj.paySlip("$800")
obj.payment("$800")
