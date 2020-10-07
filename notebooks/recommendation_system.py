import pandas as pd
import numpy as np
from surprise import Reader, Dataset
from surprise.model_selection import cross_validate, train_test_split
from surprise.prediction_algorithms import SVD
from surprise import accuracy
popular_movies_df = pd.read_csv('popular_movies.csv')
ratings_df = pd.read_csv('ratings_limited_users.csv', usecols=['userId', 'movieId', 'rating'])
movies_df = pd.read_csv('movies.csv')
# Initializing a reader and data class
reader = Reader()
data = Dataset.load_from_df(ratings_df, reader)

# Splitting the data into train and test sets
trainset, testset = train_test_split(data, test_size=.25)

# Using the tuned parameters for the SVD model
svd = SVD(n_factors=100,
               n_epochs=30,
               lr_all=0.01, 
               reg_all=0.1)
svd.fit(trainset)
svd_preds = svd.test(testset)
# Function to get new users preferences on any movie or a particular genre
def movie_rater(movie_df, num=5, genre=None):
    """ This function is to handle a cold start with a new user.  It takes in a number of ratings
        from a new user and gives the output of 5 movie recommendations.
        
        Args:
            movie_df(dataframe): the dataframe of movies that you will use to recommend movies
            num(integer): the number of ratings you want the user to input before giving a recommendation. The default value is 5.
            genre(string): The genre of movies that you wish to pull from for your user to rate.  The default is None.
        
        Returns:
            The output is a list of 5 movies with their titles and genres receommended for the user based on their initial ratings given.  
            A collaborative filter is used to add their ratings to the inital dataframe to then find this output."""
    userID = 1000
    rating_list = []
    while num > 0:
        if genre:
            movie = popular_movies_df[popular_movies_df['genres'].str.contains(genre)].sample(1)
        else:
            movie = popular_movies_df.sample(1)
        print(movie['title'])
        try: 
            rating = input('How do you rate this movie on a scale of (low)1-5(high). Press n if you have not seen this movie: \n')
            if rating == 'n':
                continue
            else:
                rating_one_movie = {'userId': userID, 'movieId': movie['movieId'].values[0], 'rating': rating}
                rating_list.append(rating_one_movie)
                num -=1
        except:
            continue
    new_ratings_df = ratings_df.append(rating_list, ignore_index=True)
    new_data = Dataset.load_from_df(new_ratings_df, reader)
    svd_ =  SVD(n_factors=100,
               n_epochs=30,
               lr_all=0.01, 
               reg_all=0.1)
    svd_.fit(new_data.build_full_trainset())
    list_of_movies = []
    for m_id in ratings_df['movieId'].unique():
        list_of_movies.append( (m_id, svd_.predict(1000, m_id)[3]))
    ranked_movies = sorted(list_of_movies, key=lambda x: x[1], reverse=True)
    n=5
    for idx, rec in enumerate(ranked_movies):
        title = movie_df.loc[movie_df['movieId'] == int(rec[0])]['title']
        print('------------------------------------------------')
        print('Recommendation # ', idx+1, ': ', title, '\n')
        n-=1
        if n==0:
            break
    
    return 
movie_rater(movies_df, 5, genre = 'Drama')
