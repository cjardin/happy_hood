from db_con import get_db_instance

import multiprocessing
from multiprocessing import Pool
import json

configs = {}
with open("pop_specs.json", "r") as a:
    configs = json.loads(a.read())

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

def runner(id_range):
    db, cur = get_db_instance()

    cur.execute(f"""update  {configs['setup']['create table name']}  
                set state = run_tick(state, house_hold_type) where h_id >= {id_range[0]} and h_id <= {id_range[1]}""")
    db.commit()
    return 1


if __name__ == "__main__":
    db, cur = get_db_instance()

    pop_size = int(configs["population count"])

    chunks = split( range(pop_size) ,  multiprocessing.cpu_count() )

    jobs = []
    for c in chunks:
        jobs.append( (c[0], c[-1] ) )

    with Pool() as p:
        print(p.map(runner, jobs))



