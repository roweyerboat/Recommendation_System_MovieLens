# Recommendation System Project
Recommendation System using Movielens data

This project uses the Grouplens Movielens database to create a recommendation system using collaborative filtering.  I utilized the surprise library to create this system.  I addressed the cold start problem with creating a function that gathers new users ratings of some of the more popular movies to be able to recommend five movies to them.  

The repository contains the following:
- [Notebook](https://github.com/roweyerboat/Recommendation_System_MovieLens/blob/master/notebooks/MovieLensRecommendation%20EDA%20and%20Model%20Building.ipynb) about the Exploratory Data Analysis of the data provided with the movielens database as well as trying out different algorithms for models
- [Notebook](https://github.com/roweyerboat/Recommendation_System_MovieLens/blob/master/Recommendation%20System.ipynb) containing how to get new users to supply ratings to address the cold start problem and using those inital ratings to recommend 5 movies
- The [data](https://github.com/roweyerboat/Recommendation_System_MovieLens/tree/master/data) from movielens (ratings.csv, movies.csv, tags.csv, links.csv)
- The [subsample](https://github.com/roweyerboat/Recommendation_System_MovieLens/tree/master/data) of data I used by filtering out users that had not rated more than 50 movies and movies that had less ratings. (ratings_limited_users.csv, popular_movies.csv)

In the end I found SVD to be the most accurate algorithm.

I addressed the cold start problem by giving new users a way to give their ratings to movies and then return 5 movie recommendations based on their ratings.  I was able to improve this process by reducing the random list of movies that they would be asked to rate to be from the most popular movies or movies that had received the most ratings.  This was to ensure that new users wouldn't be bogged down with having to go through their rating submissions filled with obscure movie titles.

Also included is an [summary presentation](https://github.com/roweyerboat/Recommendation_System_MovieLens/blob/master/Recommendation%20Systems%20Presentation.pdf). A video of this presentation can be found [here](https://drive.google.com/file/d/1CufN3AWngz1lfjzjheTf2Aqhgym10Yvt/view?usp=sharing)

Here is the link to the blog I wrote while completing this project: https://roweyerboat.github.io/the_helpful_library_of_surprise
