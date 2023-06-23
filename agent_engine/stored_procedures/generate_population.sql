CREATE OR REPLACE FUNCTION generate_population(json_configs text, drop_table_first boolean) RETURNS text
AS $$
    from happyhoodagents.agent_loader import agent_loader
    import json

    configs = json.loads(json_configs)

    def create_population(name, node, agent_count):

        if  "sub populations" not in node:
            for i in range(agent_count):
                new_agent = agent_loader( name, json.dumps(node) )

                cursor = plpy.execute(f"""insert into {configs['setup']['create table name']} 
                        (house_hold_type, state) values ( '{name}', '{json.dumps(new_agent.state).replace("'", "''")}' )""")
            return
        for sub_pop in node["sub populations"]:
            create_population( f"{name}.{sub_pop['name']}", node[ sub_pop['name'] ] , round(float( sub_pop[ "percent total population"]) *  agent_count) )
            

    #First.. Let's createe the table!
    if drop_table_first :
        cursor = plpy.execute(f"DROP TABLE IF EXISTS {configs['setup']['create table name']}")
    cursor = plpy.execute(f"CREATE TABLE {configs['setup']['create table name']} {configs['setup']['column spec']}")

    #Create 
    for pop in configs['populations']:
         create_population( pop['name'], configs[ pop['name'] ],  round(float( configs["population count"] ) * float( pop["percent total population"]) ) )

    return "good"
$$ LANGUAGE plpython3u;

