CREATE OR REPLACE FUNCTION death_tick(state json, class_name text, death_age float) RETURNS json
IMMUTABLE
PARALLEL SAFE
AS $$
    from happyhoodagents.agent_loader import agent_loader
    import json

    agent = agent_loader( class_name, state, False)

    return json.dumps( agent.agent_class.process_death( death_age ) )


$$ LANGUAGE plpython3u;

