import threading
import requests
from bs4 import BeautifulSoup
import json
import time

#search_term = input("What product do you want to search for?: ")

# https://www.imdb.com/search/title/?release_date=1980-01-01,2022-10-14&user_rating=7.0,10.0&genres=action
# https://www.imdb.com/search/title/?release_date=1980-01-01,2022-10-14&user_rating=8.0,10.0&genres=action&groups=top_100
# url = f"https://www.newegg.ca/p/pl?d={search_term.replace(' ', '+')}"

#url = f"https://www.imdb.com/search/title/?release_date={search_term.replace(' ', ',')}"

url = "https://www.imdb.com/search/title/?release_date=1980-01-01,2022-10-14&user_rating=8.0,10.0&groups=top_1000&start=151&ref_=adv_nxt"

page = requests.get(url).text

#print(page)

# lxml
soup = BeautifulSoup(page, 'html.parser')
# print(doc.prettify())
# exit()
# title, year, rating, metascore, votes, gross, director, actors, runtime, genre, description
movie_data = soup.find_all("div", class_ = "lister-item mode-advanced")

movie_title = movie_data.h3.a.text
movie_year = soup.find("span", class_ = "lister-item-year text-muted unbold").text.strip("()")
movie_rating = soup.find("div", class_ = "inline-block ratings-imdb-rating").strong.text
metascore = soup.find("div", class_ = "inline-block ratings-metascore").text.strip()[:2]
votes = soup.find_all("span", attrs= {"name" : "nv"})[0].text
gross = soup.find_all("span", attrs= {"name" : "nv"})[1].text
director = soup.find("p", attrs = {"class" : ""}).find("a").text
#actors = soup.find("p", attrs = {"class" : ""}).find("a").get("href")
runtime = soup.find("span", class_ = 'runtime').text
genre = soup.find("span" ,class_ = "genre").text.strip()
descrption = soup.find_all("p", class_ = "text-muted")[1].text.strip()
#print(page_te



movie_info = {}

for index, my_list in enumerate(movie_data):
    movie_data = soup.find_all("div", class_ = "lister-item mode-advanced")

    movie_title = movie_data.h3.a.text
    movie_year = soup.find("span", class_ = "lister-item-year text-muted unbold").text.strip("()")
    movie_rating = soup.find("div", class_ = "inline-block ratings-imdb-rating").strong.text
    metascore = soup.find("div", class_ = "inline-block ratings-metascore").text.strip()[:2]
    #votes = soup.find_all("span", attrs= {"name" : "nv"})[0].text
    #gross = soup.find_all("span", attrs= {"name" : "nv"})[1].text
    director = soup.find("p", attrs = {"class" : ""}).find("a").text
    #actors = soup.find("p", attrs = {"class" : ""}).find("a").get("href")
    runtime = soup.find("span", class_ = 'runtime').text
    genre = soup.find("span" ,class_ = "genre").text.strip()
    descrption = soup.find_all("p", class_ = "text-muted")[1].text.strip()
   
    movie_info[index+1] = {
        'Movie Title': movie_title, 
        'Year': movie_year, 
        'Rating': movie_rating, 
        'Metascore': metascore,
        'Director' : director, 
        'Runtime' : runtime,
        'Genre' : genre,
        'Description' : descrption
        }




movie_info = sorted(movie_info.items(), key = lambda x: x[1]["rating"])
items_found = dict(movie_info)

with open("items.json", "w") as file:
    json.dump(items_found, file, indent=4)

print("Done")