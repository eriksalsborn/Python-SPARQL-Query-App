sparql_query = """
    PREFIX dbp: <http://dbpedia.org/property/>
    PREFIX dbr: <http://dbpedia.org/resource/>
    PREFIX dbo: <http://dbpedia.org/ontology/>

    SELECT ?film ?gross ?distributor ?durationInMinutes
    WHERE {
    ?film dbo:writer dbr:Christopher_Nolan ;
            dbp:director dbr:Christopher_Nolan ;
            dbo:starring dbr:Christian_Bale ;
            dbo:gross ?grossUri ;
            dbo:distributor ?distributor ;
            dbo:runtime ?runtime .
    
    BIND(xsd:decimal(?runtime) / 60 AS ?durationInMinutes)
    BIND(xsd:decimal(?grossUri) AS ?gross)
    
    FILTER (?gross > 4E7)
    }
    ORDER BY DESC(?gross)
    """