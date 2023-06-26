CREATE OR REPLACE FUNCTION run_tick(state text, class_name text) RETURNS json
IMMUTABLE
PARALLEL SAFE
AS $$
    from happyhoodagents.agent_loader import agent_loader
    import json

    agent = agent_loader( class_name, state )

    agent.execute_tick()

    return json.dumps(agent.state)

$$ LANGUAGE plpython3u;
