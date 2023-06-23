select * from generate_population('{
    "setup": {
        "create table name" : "hello_usa",
        "column spec" : "(h_id uuid PRIMARY KEY DEFAULT gen_random_uuid(), house_hold_type text, state json)",
        "state column name" : "state"
    },
    "populations" : [
                        {"name" : "married", "percent total population" : ".482"},
                        {"name" : "single male", "percent total population" : ".048"},
                        {"name" : "single female", "percent total population" : ".129"},
                        {"name" : "individual", "percent total population" : ".277"},
                        {"name" : "non family", "percent total population" : ".064"}
    ],
    "population count" : "130",
    "married" : {
                    "sub populations" : [
                                            { "name" : "dual income" , "percent total population": ".53" },
                                            { "name" : "single income" , "percent total population": ".47" }
                                        ],
                    "dual income": {
                    },
                    "single income": {
                    }
    },
    "single male" : {
                        "sub populations" : [
                                                { "name" : "base" , "percent total population": "1" }
                                            ],
                        "base" : {}
                    
    },
    "single female" : {
                        "sub populations" : [
                                                { "name" : "base" , "percent total population": "1" }
                                            ],
                        "base" : {}
                    
    },
    "individual" : {
                        "sub populations" : [
                                                { "name" : "base" , "percent total population": "1" }
                                            ],
                        "base" : {}
                    
    },
    "non family" : {
                        "sub populations" : [
                                                { "name" : "base" , "percent total population": "1" }
                                            ],
                        "base" : {}
                    
    }
}', true);
