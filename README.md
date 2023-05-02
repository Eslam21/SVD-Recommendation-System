# 🎥 Movie Recommendation System using Singular Value Decomposition (SVD) 🍿

This is a movie recommendation system based on Singular Value Decomposition (SVD). It uses the Full MovieLens Dataset, which contains metadata for all 45,000 movies listed in the dataset. The dataset also contains 26 million ratings from 270,000 users for all 45,000 movies. Ratings are on a scale of 1-5 and have been obtained from the official GroupLens website.

## 📊 Dataset 

The dataset used files contain metadata for all 45,000 movies listed in the Full MovieLens Dataset. The dataset consists of movies released on or before July 2017. Data points include cast, crew, plot keywords, budget, revenue, posters, release dates, languages, production companies, countries, TMDB vote counts and vote averages.

## 💻 Implementation 

The system is built using Python and several libraries, including Pandas, Scipy, and Streamlit. Scipy's SVD implementation is used to decompose the rating matrix and obtain latent features for each movie and user. These latent features are used to generate recommendations for each user. 

## 🚀 Deployment 

The app is deployed on Streamlit. Users can input a movie title and receive a list of recommended movies. The app also displays information about the input movie, including the name and poster. 

## 📈 Performance 

The system has been tested on a subset of the dataset and has shown good performance, generating relevant and diverse recommendations for each user.   

It resultled a Mean squared error of **00.84**

## 📚 Resources 

For more information about Singular Value Decomposition, check out these resources:
- [Wikipedia](https://en.wikipedia.org/wiki/Singular_value_decomposition)
- [Introduction to Singular Value Decomposition](https://blog.statsbot.co/singular-value-decomposition-tutorial-52c695315254)
- [Recommendation Systems: Principles, Methods, and Evaluation](https://www.springer.com/gp/book/9783319296579) - a comprehensive book on recommendation systems that covers a range of methods, including matrix factorization and collaborative filtering.
- [Matrix Factorization Techniques for Recommender Systems](https://dl.acm.org/doi/abs/10.1145/1608565.1608614) - a research paper that discusses the use of matrix factorization for recommendation systems, with a focus on SVD.
- [Building a Movie Recommendation System with SVD](https://towardsdatascience.com/building-a-movie-recommendation-system-with-svd-5f972f723857) - a tutorial on building a movie recommendation system with SVD, using the MovieLens dataset.
- [MovieLens Dataset](https://grouplens.org/datasets/movielens/) - the official website for the MovieLens dataset, which includes several different versions of the dataset.
- [Collaborative Filtering for Implicit Feedback Datasets](http://yifanhu.net/PUB/cf.pdf) - a research paper that proposes a matrix factorization method specifically designed for implicit feedback datasets, such as the MovieLens dataset.

I hope these resources are helpful for anyone interested in learning more about recommendation systems and SVD!



<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Singular_value_decomposition_visualisation.svg/1200px-Singular_value_decomposition_visualisation.svg.png" alt="Image description" width="400"/>


Above is an illustration of the Singular Value Decomposition process, which decomposes a matrix into its constituent singular values and vectors. This process is used in the recommendation system to identify latent features that are used to generate recommendations for each user.
