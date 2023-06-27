import json
from numpy.random import default_rng
import random

def gen_random_from_node(node):
    rng = default_rng()

    #there might be a better way of doing this.. but I liked this approach
    index = 0;
    choice = []
    for p in node ['population_probability']:
        choice += [index] * round( float(p) * 1000)
        index += 1

    pop = random.choice( choice )
    rand_num = 0
    if node['distribution_type'][pop].lower() == 'normal':
        rand_num = rng.normal( loc=float(node['distribution_params'][pop][0]), scale=float(node['distribution_params'][pop][1]) )
    elif node['distribution_type'][pop].lower() == 'power':
        rand_num = rng.power(float(node['distribution_params'][pop][0])) * float(node['distribution_params'][pop][1])


    return (rand_num, node['population_names'][pop])

if __name__ == "__main__":

    node = {
        "population_probability" : [ ".20", ".60" , ".20"],
        "population_names" : [ "poverty", "middle", "upper"],
        "distribution_type" : ["normal", "normal", "power"],
        "distribution_params" : [ [ "40000", "20000"], ["70784", "20000"], ["5", "1000000"] ]
        }

    print(gen_random_from_node(node))
        

