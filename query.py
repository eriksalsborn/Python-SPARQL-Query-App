from util import format_input

def get_movies_by_director(director_name):
    return f"""
        PREFIX dbp: <http://dbpedia.org/property/>
        PREFIX dbr: <http://dbpedia.org/resource/>
        PREFIX dbo: <http://dbpedia.org/ontology/>

        SELECT ?filmName, 
            (GROUP_CONCAT(DISTINCT ?directorName; separator=" | ") AS ?directorName),
            (GROUP_CONCAT(DISTINCT ?allActorsName; separator=" | ") AS ?allActorsName),
            (MAX(?durationInMinutes) AS ?durationInMinutes),
            (MAX(?gross) AS ?gross),
            (MAX(?distributorName) AS ?distributorName)
        WHERE {{
            ?film dbp:name ?filmName .

            OPTIONAL {{ 
                ?film dbo:director ?director . 
                ?director dbp:name ?directorName .
            }}

            OPTIONAL {{ 
                ?film dbp:starring ?allActorsName .
            }}

            OPTIONAL {{ 
                ?film dbo:distributor ?distributor . 
                ?distributor dbp:name ?distributorName .
            }}

            OPTIONAL {{ 
                ?film dbo:runtime ?runtime .
                BIND(xsd:decimal(?runtime) / 60 AS ?durationInMinutes)
            }}

            OPTIONAL {{
                ?film dbo:gross ?grossUri . 
                BIND(xsd:decimal(?grossUri) AS ?gross)
            }}

            FILTER(regex(?directorName, "{director_name}", "i"))
        }}
        GROUP BY ?filmName
        ORDER BY DESC(?gross)
    """


def get_movies_by_actor(actor_name):
    return f"""
        PREFIX dbp: <http://dbpedia.org/property/>
        PREFIX dbr: <http://dbpedia.org/resource/>
        PREFIX dbo: <http://dbpedia.org/ontology/>

        SELECT ?filmName, 
            (GROUP_CONCAT(DISTINCT ?directorName; separator=" | ") AS ?directorName),
            (GROUP_CONCAT(DISTINCT ?allActorsName; separator=" | ") AS ?allActorsName),
            (MAX(?durationInMinutes) AS ?durationInMinutes),
            (MAX(?gross) AS ?gross),
            (MAX(?distributorName) AS ?distributorName)
        WHERE {{
            ?film dbp:name ?filmName .

            OPTIONAL {{ 
                ?film dbo:director ?director . 
                ?director dbp:name ?directorName .
            }}

            OPTIONAL {{ 
                ?film dbp:starring ?allActorsName .
                ?film dbp:starring ?searchActor .
            }}

            OPTIONAL {{ 
                ?film dbo:distributor ?distributor . 
                ?distributor dbp:name ?distributorName .
            }}

            OPTIONAL {{ 
                ?film dbo:runtime ?runtime .
                BIND(xsd:decimal(?runtime) / 60 AS ?durationInMinutes)
            }}

            OPTIONAL {{
                ?film dbo:gross ?grossUri . 
                BIND(xsd:decimal(?grossUri) AS ?gross)
            }}

            FILTER(regex(?searchActor, "{actor_name}", "i"))
        }}
        GROUP BY ?filmName
        ORDER BY DESC(?gross)
    """

def get_info_about_movie(movie_name):
    return f"""
        PREFIX dbp: <http://dbpedia.org/property/>
        PREFIX dbr: <http://dbpedia.org/resource/>
        PREFIX dbo: <http://dbpedia.org/ontology/>

        SELECT ?filmName, 
            (GROUP_CONCAT(DISTINCT ?directorName; separator=" | ") AS ?directorName),
            (GROUP_CONCAT(DISTINCT ?allActorsName; separator=" | ") AS ?allActorsName),
            (MAX(?durationInMinutes) AS ?durationInMinutes),
            (MAX(?gross) AS ?gross),
            (MAX(?distributorName) AS ?distributorName)
        WHERE {{
            ?film dbp:name ?filmName .

            OPTIONAL {{ 
                ?film dbo:director ?director . 
                ?director dbp:name ?directorName .
            }}

            OPTIONAL {{ 
                ?film dbp:starring ?allActorsName .
            }}

            OPTIONAL {{ 
                ?film dbo:distributor ?distributor . 
                ?distributor dbp:name ?distributorName .
            }}

            OPTIONAL {{ 
                ?film dbo:runtime ?runtime .
                BIND(xsd:decimal(?runtime) / 60 AS ?durationInMinutes)
            }}

            OPTIONAL {{
                ?film dbo:gross ?grossUri . 
                BIND(xsd:decimal(?grossUri) AS ?gross)
            }}

            FILTER(regex(?filmName, "{movie_name}", "i"))
        }}
        GROUP BY ?filmName
        ORDER BY DESC(?gross)
    """




