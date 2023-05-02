# from streamlit import cache
import requests
from IPython.display import Image, HTML, display
import itertools
# @cache

def movie_display(popular_movies, id:int):
    
 """This function displays movies in html and css format

Keyword arguments:
popular_movies -- movies metadata
id -- user id
Return: return_description
 """
 img=[] # to store images links 
 captions=[]  # to store images captions
 getList_name = {}
 for x, xRows in popular_movies.iterrows():

    getResponse = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c0bda0be71f7815fd6ba2eb5f5c86fd8'.format(xRows['id']) ) # every movie has a unique ID 
    getData = getResponse.json() # we request the data from the API and convert it to json
    
    # a bug fixed because sometimes there are is no poster so it returrns error
    if getData['poster_path']==None:
     continue
    else:   
     getPath = "http://image.tmdb.org/t/p/w500" + getData['poster_path']    # get the path of the poster
     getList_name[xRows['title']] = getPath
     

 for i in range(0,len(getList_name),5):

        img.append(list(getList_name.values())[i])
        img.append(list(getList_name.values())[i+1])
        img.append(list(getList_name.values())[i+2]) 
        img.append(list(getList_name.values())[i+3])
        img.append(list(getList_name.values())[i+4])

        captions.append(list(getList_name.keys())[i])
        captions.append(list(getList_name.keys())[i+1])
        captions.append(list(getList_name.keys())[i+2])
        captions.append(list(getList_name.keys())[i+3])
        captions.append(list(getList_name.keys())[i+4])
        
        
 return img,captions


# a function that puts images next to eachother
def paginator(items, items_per_page=26):
    # Display a pagination selectbox in the specified location.
    items = list(items)
    # Iterate over the items in the page to let the user display them.
    return itertools.islice(enumerate(items), 0, 26)