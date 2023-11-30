def get_movies_by_director(director_name):
    return f"""
        PREFIX dbp: <http://dbpedia.org/property/>
        PREFIX dbr: <http://dbpedia.org/resource/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        
        SELECT ?filmName 
        (GROUP_CONCAT(?allActorsName; separator=",") AS ?allActorsName)
        ?distributorName
        ?gross 
        ?durationInMinutes
        WHERE {{
            ?film dbp:director dbr:{director_name.replace(" ", "_")} ;
                dbo:gross ?grossUri ;
                dbo:distributor ?distributor ;
                dbo:runtime ?runtime ;
                dbp:name ?filmName ;
                dbo:starring ?allActors .
    
            ?distributor dbp:name ?distributorName .
            ?allActors dbp:name ?allActorsName .
    
            BIND(xsd:decimal(?runtime) / 60 AS ?durationInMinutes)
            BIND(xsd:decimal(?grossUri) AS ?gross)
    
            FILTER (?gross > 4E7)
        }}
        GROUP BY ?filmName ?distributorName ?gross ?durationInMinutes
        ORDER BY DESC(?gross)
    """