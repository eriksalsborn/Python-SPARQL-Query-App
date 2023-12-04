from util import format_input

def get_movies_by_director(director_name):
    return f"""
        PREFIX dbp: <http://dbpedia.org/property/>
        PREFIX dbr: <http://dbpedia.org/resource/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        
        SELECT ?filmName, 
        (GROUP_CONCAT(DISTINCT ?directorName; separator=",") AS ?directorName),
        (GROUP_CONCAT(DISTINCT ?allActorsName; separator=",") AS ?allActorsName),
        (GROUP_CONCAT(DISTINCT ?distributorName; separator=",") AS ?distributorName),
        ?gross,
        ?durationInMinutes
        WHERE {{
            ?film dbo:gross ?grossUri ;
                dbo:distributor ?distributor ;
                dbo:runtime ?runtime ;
                dbp:name ?filmName ;
                dbo:starring ?allActors ;
                dbo:director ?director .
    
            ?distributor dbp:name ?distributorName .
            ?allActors dbp:name ?allActorsName .
            ?director dbp:name ?directorName .
    
            BIND(xsd:decimal(?runtime) / 60 AS ?durationInMinutes)
            BIND(xsd:decimal(?grossUri) AS ?gross)

            FILTER(regex(?director, "{format_input(director_name)}", "i"))
        }}
        GROUP BY ?filmName ?gross ?durationInMinutes
        ORDER BY DESC(?gross)
    """


def get_movies_by_actor(actor_name):
    return f"""
        PREFIX dbp: <http://dbpedia.org/property/>
        PREFIX dbr: <http://dbpedia.org/resource/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        
        SELECT ?filmName, 
        (GROUP_CONCAT(DISTINCT ?directorName; separator=",") AS ?directorName),
        (GROUP_CONCAT(DISTINCT ?allActorsName; separator=",") AS ?allActorsName),
        (GROUP_CONCAT(DISTINCT ?distributorName; separator=",") AS ?distributorName),
        ?gross,
        ?durationInMinutes
        WHERE {{
            ?film dbo:gross ?grossUri ;
                dbo:distributor ?distributor ;
                dbo:runtime ?runtime ;
                dbp:name ?filmName ;
                dbp:starring ?allActors .
    
            ?distributor dbp:name ?distributorName .
            ?allActors dbp:name ?allActorsName .
            ?director dbp:name ?directorName .
    
            BIND(xsd:decimal(?runtime) / 60 AS ?durationInMinutes)
            BIND(xsd:decimal(?grossUri) AS ?gross)

            FILTER(regex(?allActors, "{format_input(actor_name)}", "i"))
        }}
        GROUP BY ?filmName ?gross ?durationInMinutes
        ORDER BY DESC(?gross)
    """

def get_info_about_movie(movie_name):
    return f"""
        PREFIX dbp: <http://dbpedia.org/property/>
        PREFIX dbo: <http://dbpedia.org/ontology/>

        SELECT ?filmName, 
            (GROUP_CONCAT(DISTINCT ?directorName; separator=",") AS ?directorName),
            (GROUP_CONCAT(DISTINCT ?allActorsName; separator=",") AS ?allActorsName),
            (GROUP_CONCAT(DISTINCT ?distributorName; separator=",") AS ?distributorName),
            ?gross,
            ?durationInMinutes
        WHERE {{
            ?film dbo:gross ?grossUri ;
                dbo:distributor ?distributor ;
                dbo:runtime ?runtime ;
                dbp:name ?filmName ;
                dbp:starring ?allActors .

            ?distributor dbp:name ?distributorName .
            ?allActors dbp:name ?allActorsName .
            ?director dbp:name ?directorName .

            BIND(xsd:decimal(?runtime) / 60 AS ?durationInMinutes)
            BIND(xsd:decimal(?grossUri) AS ?gross)

            FILTER(regex(?filmName, "{movie_name}", "i"))
        }}
        GROUP BY ?filmName ?gross ?durationInMinutes
        ORDER BY DESC(?gross)
    """


