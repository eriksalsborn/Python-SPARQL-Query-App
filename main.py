from SPARQLWrapper import SPARQLWrapper, JSON
import configparser
import pandas as pd
from query import sparql_query 

def query_dbpedia(query, sparql_endpoint):
    sparqlEndpoint = SPARQLWrapper(sparql_endpoint)
    sparqlEndpoint.setQuery(query)
    sparqlEndpoint.setReturnFormat(JSON)
    results = sparqlEndpoint.query().convert()

    bindings = results['results']['bindings']
    results_df = pd.json_normalize(bindings)

    return results_df

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    sparql_endpoint = config['SPARQL']['endpoint']

    results_df = query_dbpedia(sparql_query, sparql_endpoint)
    display_df = results_df[['film.value', 'gross.value', 'distributor.value', 'durationInMinutes.value']]
    display_df.columns = ['Film', 'Gross', 'Distributor', 'Duration (minutes)']
    print(display_df)

if __name__ == "__main__":
    main()