# Problem Statement

## Problem
Users face a large number of movies and find it hard to decide what to watch next. Browsing a full list by hand is slow, and plain rating charts ignore personal taste.

## Scope
The project is a command-line application that:
- loads a movie catalogue (title, year, genres, rating) from a CSV file,
- lets the user browse, search and filter it,
- ranks movies by rating,
- records the user's own ratings (1-5) and stores them between runs,
- recommends unseen movies using a content-based (genre affinity) method,
- finds movies similar to a chosen movie.

Out of scope: a graphical or web interface, multi-user collaborative filtering, live online data, and user authentication.

## Target Users
- Casual movie watchers who want quick suggestions.
- Students learning how a basic recommendation system works.

## High-Level Features
1. Catalogue browsing: list all, search by title, filter by genre, filter by minimum rating.
2. Ranking: top-N movies using a merge sort.
3. Personal profile: rate movies, view ratings, persistent JSON storage.
4. Recommendations: personalised suggestions and "similar movies".
5. Reliability: input validation, data validation, error handling and logging.
