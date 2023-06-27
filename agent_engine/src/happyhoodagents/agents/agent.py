import json
from happyhoodagents.random_tools import gen_random_from_node
import random

class agent:
    def __init__(self, state):
        state = json.loads( state)
        new_state = { "stats" : {} }
        new_state['stats']['income'] =  gen_random_from_node( state['income'] )

        individuals = []
        for i in range( int( random.choice(state['individuals']['total']) )):
            individuals.append( gen_random_from_node( state['individuals']["age"] ) )
        

        new_state['stats']['individuals'] = len(individuals)
        new_state['stats']['ages'] = individuals
        self.state = new_state

    def execute_tick(self):
        return self.state

    def clear_class_change(self):
        return self.state
    



        

