import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309', headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')


songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for song in songs:
    rank = song.select_one('td.number')
    title = song.select_one('td.info > a.title.ellipsis')
    singer = song.select_one('td.info > a.artist.ellipsis')
    if title is not None:
        print (rank.text, title.text, singer.text)