# SPARQL-Movie-Explorer

This Python script leverages the SPARQLWrapper library to interact with the DBpedia SPARQL endpoint, allowing users to retrieve information about movies featuring a particular actor or director. The script constructs a SPARQL query that fetches details such as movie names, directors, co-actors, duration, gross revenue, and distributor names.

## Key Components

**SPARQL Query:** The script defines a SPARQL query using PREFIX clauses for namespaces and constructs a pattern to select relevant movie information. It uses OPTIONAL clauses to handle optional data such as directors, distributors, and runtime.

**SPARQLWrapper:** The SPARQLWrapper library is employed to set up the SPARQL endpoint URL, inject the query, and specify the desired return format (JSON in this case).

**Execution and Results:** The script executes the query against the DBpedia SPARQL endpoint and retrieves the results in JSON format. The results can be further processed, analyzed, or presented based on the specific needs of the application.

![demo](demo.gif)

## Installation

1. **Clone the repository:**
 ```bash
 git clone git@github.com:eriksalsborn/SPARQL-Movie-Explorer.git
 ```

2. **Navigate to the project directory**
```bash
   cd SPARQL-Movie-Explorer
```
3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

This will install the required Python packages for the project.

## Usage 

1. **Run the script:**
```bash
   python main.py
```
2. **Enter 'd', 'a' or 'm' to specify whether you want to search by actor's/actress's or by director's name.**

3. **Enter the name**

Voila! If any movies are found, they will be displayed along with some interesting facts about the movies.
