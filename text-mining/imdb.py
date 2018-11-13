from imdbpie import Imdb

imdb = Imdb()
print(imdb.search_for_title("Bohemian Rhapsody")[0])
reviews = imdb.get_title_user_reviews("tt1727824")

import pprint
pprint.pprint(reviews)

# print(reviews['reviews']['author']['displayName'])
print(reviews['reviews']['reviewText'])
