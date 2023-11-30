from SPARQLWrapper import SPARQLWrapper, JSON
import configparser
import pandas as pd
from query import get_movies_by_director, get_movies_by_actor

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

def perform_movie_search(sparql_endpoint):
    while True:
        actor_or_director = input("Do you want to search movies for directors or actors? (d/a): ").lower()

        if actor_or_director not in ['d', 'a']:
            print("Invalid input. Please enter 'd' for directors or 'a' for actors.")
            continue

        name_type = "director's" if actor_or_director == 'd' else "actor's/actress'"
        name_input = input(f"Enter {name_type} name: ")

        query_function = get_movies_by_director if actor_or_director == 'd' else get_movies_by_actor

        results = query_dbpedia(query_function(name_input), sparql_endpoint)
        display_results(results, name_input)

        another_search = input("Do you want to perform another search? (y/n): ").lower()
        if another_search != 'y':
            break

def main():
    sparql_endpoint = get_sparql_endpoint()
    perform_movie_search(sparql_endpoint)

if __name__ == "__main__":
    main()
