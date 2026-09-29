# Movie Recommendation System

A command-line movie recommender written in Python. It lets you browse a movie catalogue, rate movies, and get personalised suggestions based on the genres you like.

## Overview
Movies are stored in `data/movies.csv`. When you rate movies from 1 to 5, the program builds a genre "taste profile" (ratings above 3 raise a genre's score, ratings below 3 lower it) and ranks the movies you have not rated by how well they match. It can also find movies that are similar to one you pick, using genre overlap (Jaccard similarity). See [statement.md](statement.md) for the problem statement, scope and target users.

## Features
- Show all movies, search by title, filter by genre, filter by minimum rating
- Top-N highest rated movies (hand-written merge sort)
- Rate movies (1-5); ratings are saved to `data/user_ratings.json` per user name
- Personalised recommendations with a match score
- "Movies similar to..." feature
- Input validation, CSV validation, error handling and logging to `logs/app.log`

## Technologies Used
- Python 3.8 or newer (standard library only: `csv`, `json`, `logging`, `dataclasses`, `unittest`)
- Git and GitHub for version control

## Project Structure
```
movie-recommender/
├── main.py                 # entry point
├── requirements.txt
├── statement.md
├── data/
│   └── movies.csv          # movie catalogue
├── recsys/
│   ├── models.py           # Movie and UserProfile classes
│   ├── data_loader.py      # CSV reading and validation
│   ├── catalog.py          # search and filter functions
│   ├── ranking.py          # merge sort and top-N
│   ├── recommender.py      # genre affinity and similarity
│   ├── user_store.py       # saves/loads ratings as JSON
│   ├── utils.py            # logging and input helpers
│   └── cli.py              # menu and user interaction
└── tests/
    └── test_recsys.py      # unit tests
```

## Installation and Setup
1. Check that Python 3.8+ is installed:
   ```
   python --version
   ```
   (On some systems use `python3` instead of `python`.)
2. Clone the repository and enter the folder:
   ```
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```
3. (Optional) Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   ```
4. Install dependencies. There are none beyond the standard library, but this command is safe to run:
   ```
   pip install -r requirements.txt
   ```
5. No further configuration is needed. The program creates `logs/` and `data/user_ratings.json` automatically.

## Running the Project
```
python main.py
```
Enter your name when asked, then choose options from the menu (0-9).

Example session:
1. Enter option `6`, type part of a title such as `inception`, then give a rating `5`.
2. Rate at least three movies.
3. Enter option `7` to see your favourite genre and recommended movies.

## Running the Tests
```
python -m unittest discover -s tests -v
```
All tests should pass. They cover filtering, sorting, the recommender, CSV validation and saving/loading ratings.

## Design Notes
- **Modular design:** the interface (`cli.py`) is separate from the logic (`catalog`, `ranking`, `recommender`) and storage (`data_loader`, `user_store`).
- **Non-functional requirements:** usability (clear menu, default values), reliability (bad CSV rows skipped, crash-proof menu loop), maintainability (small modules with docstrings and tests), performance (merge sort in O(n log n)), error handling and logging.

## Limitations and Future Work
- The catalogue is small and rating-based only on genres.
- Possible extensions: collaborative filtering across users, more attributes (director, actors), a larger dataset, and a web or GUI front end.
