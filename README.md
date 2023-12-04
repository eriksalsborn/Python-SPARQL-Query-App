# SPARQL-Movie-Explorer

Simple straightforward Python script designed to query SPARQL endpoints and retrieve the results.

The script prompts the user to input a director's, actor's/actresse's or a movie's name. After entering the name, the script queries the SPARQL endpoint to display a list of movies that matches the speciefied input.

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