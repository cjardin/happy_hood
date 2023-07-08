import json
from happyhoodagents.random_tools import gen_random_from_node
import random

class agent:
    def __init__(self, state, init_state = False):
       
        #to hard to put into the config
        self.ageing_per_tick = .0833


        state = json.loads( state)
        if init_state:
            new_state = { "stats" : {} }
            new_state['stats']['income'] =  gen_random_from_node( state['income'] )

            individuals = []
            for i in range( int( random.choice(state['individuals']['total']) )):
                individuals.append( gen_random_from_node( state['individuals']["age"] ) )
        

            new_state['stats']['individuals'] = len(individuals)
            new_state['stats']['ages'] = individuals
            self.state = new_state
        else:
            self.state = state

    def execute_tick(self):
        for i in range( len(self.state['stats']['ages'])):
            self.state['stats']['ages'][i] = (self.state['stats']['ages'][i][0] +  self.ageing_per_tick, self.state['stats']['ages'][i][1])

        return self.state

    def process_death(self, age):

        if self.state['stats']['individuals'] == 1:
            self.state['tick_actions'] = "delete"

        #find the age and kill it.. Morbid, but intersting 
        age_to_del = None
        for a in self.state['stats']['ages']:
            if a[0] == age:
                age_to_del = a
                break

        if age_to_del != None:
            self.state['stats']['ages'].remove(age_to_del)
            self.state['stats']['individuals'] = self.state['stats']['individuals']  -1

        self.check_household_class()

        return self.state

    def check_household_class():
        pass

    def tick_actions(self):
        try:
            del self.state['tick_actions']
        except:
            pass

        return self.state
    



        

