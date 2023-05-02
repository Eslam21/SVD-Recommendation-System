# Movie Recommendation System with Singular Value Decomposition (SVD)

Welcome to my movie recommendation system! This is a project I created using singular value decomposition (SVD) to recommend movies to users based on their past ratings.

## About the Project

This recommendation system was built using Python and the Surprise library, which provides a collection of ready-to-use algorithms for collaborative filtering, including SVD. The dataset used for this project is the Full MovieLens Dataset, which contains metadata for over 45,000 movies released on or before July 2017. It also includes 26 million ratings from 270,000 users for all 45,000 movies. Ratings are on a scale of 1-5 and have been obtained from the official GroupLens website.

## How it Works

The recommendation system is based on the idea that users who have rated movies similarly in the past are likely to have similar tastes in movies, and therefore would enjoy similar movies in the future. The SVD algorithm used in this project creates a matrix factorization of the user-item rating matrix, and uses the resulting matrices to predict ratings for unrated movies by each user.

### Singular Value Decomposition

Singular value decomposition (SVD) is a powerful matrix factorization technique that is commonly used in recommender systems. SVD is a way to decompose a matrix into three other matrices, which can then be used to approximate the original matrix. The three matrices are:

- U: a matrix of left singular vectors
- Σ: a diagonal matrix of singular values
- V^T: a matrix of right singular vectors

![SVD Diagram](https://user-images.githubusercontent.com/74459082/235782376-b0bc5f78-661f-40e1-87fa-63fd01ebf205.png)

The U, Σ, and V matrices are determined through a process of matrix factorization. The diagonal values in the Σ matrix represent the importance of each dimension in the original matrix. The dimensions with the largest values are the most important.

### Matrix Factorization

Matrix factorization is the process of decomposing a matrix into its constituent parts in order to make it more understandable or easier to manipulate. In the case of the movie recommendation system, the goal is to factorize the user-item rating matrix into the U, Σ, and V matrices described above.


The SVD algorithm can then use these matrices to predict the ratings for unrated movies by each user.

### Streamlit

The system uses Streamlit to deploy the model and create a user-friendly interface. Users can input their user ID and receive a list of top recommended movies based on their past ratings. The recommendations are based on a combination of predicted ratings and popularity.

## How to Use

To use the recommendation system, you will need to download the code and the Full MovieLens Dataset from https://grouplens.org/datasets/movielens/  

Once you have the necessary files and libraries, you can run the recommendation system by running the `app.py` script and following the prompts.



## Conclusion

I hope you find this movie recommendation system useful and enjoyable! If you have any questions or suggestions for improvement, feel free to reach out.
