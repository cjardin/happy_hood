import json

#Load all agents
from happyhoodagents.agents.agent import agent
from happyhoodagents.agents.married_dual_income import married_dual_income
from happyhoodagents.agents.married_single_income import married_single_income
from happyhoodagents.agents.non_family import non_family
from happyhoodagents.agents.single_female import single_female
from happyhoodagents.agents.single_male import single_male
from happyhoodagents.agents.married import married
from happyhoodagents.agents.individual import individual

class agent_loader:
  def __init__(self, agent_class, state, init_state = False):
    self.state = json.loads(state)
    self.agent_class = agent( state, init_state)

    if agent_class == "married":
        self.agent_class = married(state, init_state)
    elif agent_class == "married.dual_income":
        self.agent_class = married_dual_income(state, init_state)
    elif agent_class == "married.single_income":
        self.agent_class = married_single_income(state, init_state)
    elif agent_class == "non_family":
        self.agent_class = non_family(state, init_state)
    elif agent_class == "single_male":
        self.agent_class = single_male(state, init_state)
    elif agent_class == "single_female":
        self.agent_class = single_female(state, init_state)        
    elif agent_class == "individual":
        self.agent_class = individual(state, init_state) 

if __name__ == "__main__":
    a = agent_loader( "foo", "{}", true)
    print(1)
        

