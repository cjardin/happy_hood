CREATE OR REPLACE FUNCTION run_tick(state json, class_name text) RETURNS json
IMMUTABLE
PARALLEL SAFE
AS $$
    from happyhoodagents.agent_loader import agent_loader
    import json

    agent = agent_loader( class_name, state, False)

    return json.dumps(agent.agent_class.execute_tick())


$$ LANGUAGE plpython3u;

