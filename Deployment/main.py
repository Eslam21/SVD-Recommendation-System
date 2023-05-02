from Displayer import movie_display,paginator
import streamlit as st
import pandas as pd


st.set_page_config(
        page_title="Movie Recommendation System",
        page_icon="🎥",
        layout="wide",
    )
@st.cache
def read_data():
    svd=pd.read_csv("SVD.csv",index_col=0)
    meta=pd.read_csv("movies_metadata.csv")
    return svd,meta


def get_recommendation(svd,meta, userid:int)-> list:

    user_ratings = svd.iloc[userid,:].sort_values(ascending=False)
    
    recommended_movies_ids=list(user_ratings.index)
    
    recommended_movies_ids = list(map(str, recommended_movies_ids))
    data=meta[meta['id'].isin (recommended_movies_ids[:100])]
    
    return data[0:25] # return first 25 movies 
    

svd,meta=read_data()

col1, col2, col3 = st.columns([1,5,1])
with col1:
    st.write("")
with col2:
    st.image("https://heartoflongmont.org/wp-content/uploads/2019/02/Movie-Recommendation.jpg", width=900)
with col3:
    st.write("")

num=st.number_input("Enter user ID ranged from 1 to 671",step=1,value=0,min_value= 0,max_value= 671)

if num>0:
    movies=get_recommendation(svd,meta,num)
    html_string=f""" <div style="font-size:34px; font-weight:Bold; color:#fff; text-align:center; padding-top:8px; height:12%; width: 100%;  margin-top:10px; background-color:#580b0f;">"Recommended Movies to user with id "{num} </div> """
    st.write(html_string, unsafe_allow_html=True)
    img,captions=movie_display(movies,num)
    with st.spinner('الصبر طيب'):
        image_iterator = paginator(img)
        indices_on_page, images_on_page = map(list, zip(*image_iterator))
        st.success('Done, hope you like the movies! 😊')
    st.image(images_on_page, width=250, caption=captions)
    
else:
    pass    





