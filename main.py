from SPARQLWrapper import SPARQLWrapper, JSON
import configparser
import pandas as pd
from query import get_movies_by_director

def get_sparql_endpoint():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['SPARQL']['endpoint']

def query_dbpedia(query, sparql_endpoint):
    sparql_wrapper = SPARQLWrapper(sparql_endpoint)
    sparql_wrapper.setQuery(query)
    sparql_wrapper.setReturnFormat(JSON)
    
    results = sparql_wrapper.query().convert()
    return results['results']['bindings']

def display_results(results, director_name):
    if results:
        results_df = pd.json_normalize(results)
        display_df = results_df[['filmName.value', 'allActorsName.value', 'gross.value', 'distributorName.value', 'durationInMinutes.value']]
        display_df.columns = ['Film', 'Actors', 'Gross', 'Distributor', 'Duration (minutes)']
        print(display_df)
    else:
        print(f"No movies found for director: {director_name}")

def main():
    sparql_endpoint = get_sparql_endpoint()
    director_name = input("Enter director's name: ")
    query = get_movies_by_director(director_name)
    results = query_dbpedia(query, sparql_endpoint)
    display_results(results, director_name)

if __name__ == "__main__":
    main()
