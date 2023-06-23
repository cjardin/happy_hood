select * from generate_population('{
    "setup": {
        "create table name" : "hello_usa",
        "column spec" : "(h_id uuid PRIMARY KEY DEFAULT gen_random_uuid(), house_hold_type text, state json)",
        "state column name" : "state"
    },
    "populations" : [
                        {"name" : "married", "percent total population" : ".482"},
                        {"name" : "single_male", "percent total population" : ".048"},
                        {"name" : "single_female", "percent total population" : ".129"},
                        {"name" : "individual", "percent total population" : ".277"},
                        {"name" : "non_family", "percent total population" : ".064"}
    ],
    "population count" : "1300",
    "married" : {
                    "sub populations" : [
                                            { "name" : "dual_income" , "percent total population": ".53" },
                                            { "name" : "single_income" , "percent total population": ".47" }
                                        ],
                    "dual_income": {
                    },
                    "single_income": {
                    }
    },
    "single_male" : {
                        "sub populations" : [
                                                { "name" : "base" , "percent total population": "1" }
                                            ],
                        "base" : {}
                    
    },
    "single_female" : {
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
    "non_family" : {
                        "sub populations" : [
                                                { "name" : "base" , "percent total population": "1" }
                                            ],
                        "base" : {}
                    
    }
}', true);
