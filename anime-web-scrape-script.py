import requests
from bs4 import BeautifulSoup
import pandas as pd


title = []
rank = []
genre = []
score = []
synopsis = []

for i in range(1,5):
    url = "https://www.imdb.com/search/keyword/?keywords=anime&mode=advanced&page={}&ref_=kw_nxt&sort=user_rating,desc".format(i)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    content = soup.find(id='main')
    anime_elements = content.find_all('div', class_='lister-item-content')




    for anime_element in anime_elements:
        # Each job_elem is a new BeautifulSoup object.
        # You can use the same methods on it as you did before.
        title_and_rank = anime_element.find('h3', class_='lister-item-header')
            
        # title
        title_element = title_and_rank.find('a').text
        # rank
        rank_element = title_and_rank.find('span', class_='lister-item-index').text.strip('.')
        # synopsis
        synopsis_element = anime_element.findAll('p', class_ ='text-muted')[1].text.strip()
        # genre
        genre_element = anime_element.find('span', class_='genre')
        if genre_element != None:
            genre_text = genre_element.text.strip()
        else:
            genre_text = "NA"
        # score
        score_element = anime_element.find('div', class_='ratings-imdb-rating')
        if score_element != None:
            score_text = score_element.text
        else:
            score_text = "NA"

        # if None in (title_and_rank, genre_element, score_element, synopsis_element):
        #     continue
        title.append(title_element)
        rank.append(rank_element)
        genre.append(genre_text)
        score.append(score_text.strip())
        synopsis.append(synopsis_element)
    

df = pd.DataFrame({'Rank':rank,'Score' : score, 'Title':title, 'Genre' : genre , 'Synopsis': synopsis}) 
df.to_csv('animeRatings.csv', index=False, encoding='utf-8')