import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi, "html.parser")

kullanici = float(input("Raiting giriniz: "))

film_isimleri = soup.find_all("td", {"class" : "titleColumn"})
ratingler = soup.find_all("td", {"class", "ratingColumn imdbRating"})

#print(len(film_isimleri), len(ratingler))

for film, rating in zip(film_isimleri, ratingler):
    film = film.text
    rating = rating.text

    film = film.strip()
    film = film.replace("\n", "")

    rating = rating.strip()
    rating = rating.replace("\n", "")


    if float(rating) > kullanici:
        print("Film ismi: {} Filmin ratingi: {}".format(film, rating))

"""
    print("Film: ", film)
    print("Rating: ", rating)
    print("-----------------------------------------")
"""