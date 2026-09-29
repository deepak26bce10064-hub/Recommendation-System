# Recommendation-System:
The program is a movie recommendation system menu lets you show all movies , get recommendations by genre , get recommendations by minimum rating , see the top 5 movies (sorted with a hand-written bubble sort) , get a personal recommendation, where you rate a few movies and it suggests unseen ones from your best genre.
# How It Works:
Movie names, genres and ratings are stored in three lists. The same position in each list belongs to the same movie.
A while loop keeps showing the menu until the user chooses Exit.
An if-elif-else block checks the user's choice and calls the matching function.
# What it does:
1	Prints all movies with genre and rating
2	Asks for a genre and prints the movies of that genre
3	Asks for a minimum rating and prints every movie at or above it
4	Sorts a copy of the ratings (highest first) and prints the top 5
5	Asks the user to rate 7 movies from 1 to 5, adds up points for each genre, finds the favourite genre, and recommends movies of that genre that the user has not rated
6	Exits the program
