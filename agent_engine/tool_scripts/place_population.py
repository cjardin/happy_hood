from db_con_prod import get_db_instance
from hh_logging import logger
import math

def place_population():
    db, cur = get_db_instance()


    logger.debug("drop exisiting placement table")
    cur.execute("drop table if exists household_to_geoid;")
    logger.debug("Create placement table")
    cur.execute("""create table household_to_geoid (h_id bigint, GEOID text);""")
    cur.execute("""create index on household_to_geoid (h_id);""")
    cur.execute("""create index on household_to_geoid (GEOID);""")

    db.commit();

    logger.debug("Compute target per geoid")
    cur.execute("""select sum("B03002EST1") as target, "GEOID" from 
            curation_sim.acs_5yr_demographic_estimate_data_by_tract group by "GEOID";""")
    for row in  cur.fetchall():

        if row[0] == None:
            continue 

        #get non accounted..
        cur.execute(f"""select a.h_id , (state->'stats'->>'individuals')::int from usa_households a LEFT JOIN household_to_geoid b ON
            a.h_id = b.h_id limit {row[0]}""")
        placed = 0
        for p in cur.fetchall():
            placed += p[1]
            cur.execute(f"""insert into household_to_geoid values ( {p[0]}, '{row[1]}');COMMIT;""")

            if placed >= (row[0] - 2):
                break    
        logger.debug(f"Placed {placed} individuals into geoid {row[1]} with target count of {row[0]}")


if __name__ == "__main__":
    place_population()
    



