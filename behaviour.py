from deck import Deck
from tokenize import String

class StaticActionCostFunction(object):
    def __init__(self):
        pass
    def list_actions(self, context) -> list():
        print("Static behaviour: ",context.budget, context.population, context.resources, context.hp, context.deck)
        return []
    
class GreedyActionCostFunction(object):
    def __init__(self):
        pass
    def list_actions(self, context) -> list():
        print("Greedy behaviour: ",context.budget, context.population, context.resources, context.hp, context.deck)
        return []
    