import json
import requests_with_caching


def get_movies_from_tastedive(string):
    baseurl = "https://tastedive.com/api/similar"
    param_diction = {}
    param_diction['q'] = string
    param_diction['type'] = 'movies'
    param_diction['limit'] = 5
    resp = requests_with_caching.get(baseurl, params = param_diction)
    page = json.loads(resp.text)
    return page


def extract_movie_titles(diction):
    movie_lst = [d['Name'] for d in diction['Similar']['Results']]
    return movie_lst

def get_related_titles(lst):
    new_lst = []
    for i in lst:
        movie_data = get_movies_from_tastedive(i)
        movie_title = extract_movie_titles(movie_data)
        for movie in movie_title:
            if movie not in new_lst:
                new_lst.append(movie)      
    return new_lst   

def get_movie_data(string):
    baseurl = 'http://www.omdbapi.com/'
    param_diction = {}
    param_diction['t'] = string
    param_diction['r'] = 'json'
    resp = requests_with_caching.get(baseurl,params = param_diction)
    page = json.loads(resp.text)
    return page

def get_movie_rating(diction):
    ratings = 0
    for d in diction['Ratings']:
        if d['Source'] == 'Rotten Tomatoes':
            ratings = int(d['Value'][:-1])
    return ratings

def get_sorted_recommendations(lst):
    diction = {}
    required = get_related_titles(lst)  
    for movie in required:
        diction[movie] = get_movie_rating(get_movie_data(movie))
    return sorted(diction, reverse = True, key = lambda x: (diction[x],x))  