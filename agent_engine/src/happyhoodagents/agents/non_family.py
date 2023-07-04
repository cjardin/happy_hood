import json
from happyhoodagents.agents.agent import agent

class non_family (agent):
    def __init__(self, state, init_state=False):
          super().__init__(state, init_state)

    def check_household_class():
        super().check_household_class()

        #Death cases
        if self.state['stats']['individuals'] == 1:
            if self.state['stats']['ages'][0] > 18: 
                self.state['tick_actions'] = "NEW HEAD"
            else:
                self.state['tick_actions'] = "ORPHAN"


        

