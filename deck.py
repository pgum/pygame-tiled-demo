
from tokenize import String
import pygame, pytmx

class Card(object):
    def __init__(self, 
                 name: String, 
                 cost_function, 
                 result_function):
        self.name=name
        self.cost_function= cost_function
        self.result_function= result_function
        
class Deck(object):
    def __init__(self):
        self.cards= []
        card1_cost= lambda x: 10
        card2_cost= lambda x: 25
        def card1_result(context):
            context.movement + 1
            return context
        def card2_result(context):
            context.movement + 3
            return context
        self.cards.append(Card("Basic movement", card1_cost, card1_result))
        self.cards.append(Card("Basic movement", card2_cost, card2_result))
        
        #self.cards.append(Card("Shord movement",  lambda context: 13*(100-context.speed)/100, lambda context: context.movement+=2*context.proficiency["movement"]*(1+(context.development/100]))))
        #self.cards.append(Card("Long movement", lambda context: 34*(110-context.speed)/100, lambda context: context.movement+=7*context.proficiency["movement"]*(1+(context.development/100]))))
        #self.cards.append(Card("Gather resources", lambda context: 25*(105-context.speed)/100, lambda context: context.resources+=17*context.proficiency["resources"]*(1+(context.development/100]))))
        #self.cards.append(Card("Develop", lambda context: 41*(221-context.speed)/222, lambda context: context.resources-=37, context.development+=7*(1+(context.development/1000]))))
        
    