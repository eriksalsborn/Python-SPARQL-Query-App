from SPARQLWrapper import SPARQLWrapper, JSON
import configparser
import pandas as pd
from query import get_movies_by_director, get_movies_by_actor, get_info_about_movie

def get_sparql_endpoint():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['SPARQL']['endpoint']

def query_dbpedia(query, sparql_endpoint):
    sparql_wrapper = SPARQLWrapper(sparql_endpoint)
    sparql_wrapper.setQuery(query)
    sparql_wrapper.setReturnFormat(JSON)

    print('\nLoading... \n')
    
    results = sparql_wrapper.query().convert()
    return results['results']['bindings']

def display_results(results, name_input):
    if results:
        results_df = pd.json_normalize(results)
        display_df = results_df[['filmName.value', 'directorName.value', 'allActorsName.value', 'durationInMinutes.value', 'gross.value', 'distributorName.value']]
        display_df.columns = ['Film', 'Director', 'Actors', 'Duration (min)', 'Gross (USD)', 'Distributor']
        print(display_df)
    else:
        print(f"No movies found for: {name_input}")

def perform_movie_search(sparql_endpoint):
    while True:
        actor_or_director_or_movie = input("Do you want to search movies by directors, actors, name of movies? (d/a/m): ").lower()

        if actor_or_director_or_movie not in ['d', 'a', 'm']:
            print("Invalid input. Please enter 'd' for directors, 'a' for actors or 'm' for movies")
            continue

        name_type = "director's" if actor_or_director_or_movie == 'd' else "actor's/actress'" if actor_or_director_or_movie == 'a' else "movie's"
        name_input = input(f"Enter {name_type} name: ")

        query_function = get_movies_by_director if actor_or_director_or_movie == 'd' else get_movies_by_actor if actor_or_director_or_movie == 'a' else get_info_about_movie

        results = query_dbpedia(query_function(name_input), sparql_endpoint)
        display_results(results, name_input)

        another_search = input("\nDo you want to perform another search? (y/n): ").lower()
        if another_search != 'y':
            break

def main():
    sparql_endpoint = get_sparql_endpoint()
    perform_movie_search(sparql_endpoint)

if __name__ == "__main__":
    main()
