# Recommendation System Project
Recommendation System using Movielens data

This project uses the Grouplens Movielens database to create a recommendation system using collaborative filtering.  I utilized the surprise library to create this system.  I addressed the cold start problem with creating a function that gathers new users ratings of some of the more popular movies to be able to recommend five movies to them.  

The repository contains the following:
- Notebook about the Exploratory Data Analysis of the data provided with the movielens database as well as trying out different algorithms for models
- Notebook containing how to get new users to supply ratings to address the cold start problem and using those inital ratings to recommend 5 movies
- The data from movielens (ratings.csv, movies.csv, tags.csv, links.csv)
- The subsample of data I used by filtering out users that had not rated more than 50 movies and movies that had less ratings. (limited_user_ratings.csv, popular_movies.csv)

In the end I found SVD to be the most accurate algorithm.

Also included is an executive summary presentation.
