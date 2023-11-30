# SPARQL-Movie-Explorer

Simple straightforward Python script designed to query SPARQL endpoints and retrieve the results.

The script prompts the user to input a director's or a actor's/actresse's name. After entering the name, the script queries the SPARQL endpoint to display a list of movies directed or played by the specified individual.

![demo](demo.gif)

## Installation

1. **Clone the repository:**
 ```bash
 git clone git@github.com:eriksalsborn/SPARQL-Movie-Explorer.git
 ```

2. **Navigate to the project directory**
```bash
   cd Python-SPARQL-Query-App
```
3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

This will install the required Python packages for the project.

4. **Configure SPARQL endpoint**
- Open the config.py file.
- Update the SPARQL_ENDPOINT variable with the URL of the SPARQL endpoint you want to query.
- It is set by default to http://dbpedia.org/sparql

## Usage 

1. **Run the script:**
```bash
   python main.py
```
2. **Enter 'd' or 'a' to specify whether you want to search by actor's/actress's or by director's name.**

3. **Enter the name for which you want to view movies.**

Voila! If any movies are found for the director, they will be displayed along with some interesting facts about the movies.
