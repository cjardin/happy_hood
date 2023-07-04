from db_con import get_db_instance

import multiprocessing
from multiprocessing import Pool
import json
import numpy as np

from happyhoodagents.random_tools import gen_random_from_node

configs = {}
with open("pop_specs.json", "r") as a:
    configs = json.loads(a.read())

def births():
    #single women, married, individual, other

    number_to_place = int(configs["per tick"]["births"])
    pass

def deaths():
    db, cur = get_db_instance()
    number_to_remove = int(configs["per tick"]["deaths"])

    counts = []
    ranges = []
    for p in range( len(configs["per tick"]["death selection"]['population_probability']) ):
        counts.append( float( configs["per tick"]["death selection"]['population_probability'][p] ) * number_to_remove )
        ranges.append( ( int( configs["per tick"]["death selection"]['population_names'][p][0]), int( configs["per tick"]["death selection"]['population_names'][p][1]) )  ) 


    for i in range( len(counts)):
        #create or age table
        cur.execute("drop table if exists death_choice");
        cur.execute(f"""
            create temp table death_choice as select h_id, abs(a.age::float) as f_age  from (select h_id, json_array_elements(state->'stats'->'ages')->>0 as age 
                from {configs['setup']['create table name']}) as  a where abs(a.age::float) > {ranges[i][0]} and 
                abs(a.age::float) <= {ranges[i][1]} ;""")
        cur.execute(f"""select h_id, f_age from death_choice order by random() limit {counts[i]}""")
        for r in cur.fetchall():
            cur.execute(f"""update {configs['setup']['create table name']}
                    set state =  death_tick(state, house_hold_type, {r[1]} ) where h_id = {r[0]}""")
    db.commit()


def merge_households():
    pass

def new_households():
    pass

def migrant():
    number_to_place = int(configs["per tick"]["migrant"])
    pass




def split(a, n): 
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

def state_update(id_range):
    db, cur = get_db_instance()

    cur.execute(f"""update  {configs['setup']['create table name']}
                set state = run_tick(state, house_hold_type) where h_id >= {id_range[0]} and h_id <= {id_range[1]}""")
    db.commit()
    return 1


def process_tick_actions(id_range):
    db, cur = get_db_instance()

    cur.execute(f"""update  {configs['setup']['create table name']}
                set state = tick_actions(state, house_hold_type) where h_id >= {id_range[0]} and h_id <= {id_range[1]}""")
    db.commit()
    return 1


def execute_parallel_update( function ):
    db, cur = get_db_instance()

    pop_size = int(configs["population count"])

    chunks = split( range(pop_size) ,  multiprocessing.cpu_count() )

    jobs = []
    for c in chunks:
        jobs.append( (c[0], c[-1] ) ) 

    with Pool() as p:
        print(p.map(function, jobs))


if __name__ == "__main__":
    #deaths()
    execute_parallel_update(process_tick_actions)
    #execute_parallel_update(state_update)
    



