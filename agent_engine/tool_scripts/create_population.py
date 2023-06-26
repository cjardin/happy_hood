from db_con import get_db_instance

import multiprocessing
from multiprocessing import Pool
import json

from happyhoodagents.agent_loader import agent_loader

configs = {}
with open("pop_specs.json", "r") as a:
    configs = json.loads(a.read())

def create_population(name, node, agent_count,cursor):
    if  "sub populations" not in node:
        for i in range(agent_count):
            new_agent = agent_loader( name, json.dumps(node) )
            cursor.execute(f"""insert into {configs['setup']['create table name']} 
                        (house_hold_type, state) values ( '{name}', '{json.dumps(new_agent.state).replace("'", "''")}' )""")
        return  

    for sub_pop in node["sub populations"]:
        create_population( f"{name}.{sub_pop['name']}", node[ sub_pop['name'] ] , round(float( sub_pop[ "percent total population"]) *  agent_count) , cursor)


def runner(shard_population_count):
    db, cur = get_db_instance()
    #Create 
    for pop in configs['populations']:
        create_population( pop['name'], configs[ pop['name'] ],  round(float( shard_population_count  ) * float( pop["percent total population"]) ), cur)
        db.commit()
         
    return 1


if __name__ == "__main__":
    db, cur = get_db_instance()

    total_pop = int(configs["population count"])
    chunks = round( total_pop / multiprocessing.cpu_count())

    #First.. Let's createe the table!
    cur.execute(f"DROP TABLE IF EXISTS {configs['setup']['create table name']}")
    cur.execute(f"CREATE TABLE {configs['setup']['create table name']} {configs['setup']['column spec']}")
    db.commit()


    jobs = [ chunks ] *  multiprocessing.cpu_count()
    with Pool() as p:
        print(p.map(runner, jobs))



