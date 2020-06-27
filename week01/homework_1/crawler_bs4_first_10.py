from utils.my_utils import log_execution_time
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


def prepare_cookie_jar():
    jar = requests.cookies.RequestsCookieJar()
    jar.set('uuid_n_v', 'v1')
    jar.set('uuid', '27C9CAD0B89711EAACB6BBD781D8993868D41D2C507D4823B251DFDC04E71EB1')
    jar.set('_csrf', '1bc54f037cd1ba0ac59ebaf73dd3f44cb090401b1a3b1d596cdee1a9bca658eb')
    jar.set('Hm_lvt_703e94591e87be68cc8da0da7cbd0be2', '1593276996')
    jar.set('_lxsdk_cuid', '172f6b59976c8-09c0241ea13f8e-4353760-e1000-172f6b59976c8'),
    jar.set('_lxsdk', '27C9CAD0B89711EAACB6BBD781D8993868D41D2C507D4823B251DFDC04E71EB1')
    jar.set('mojo-uuid', '145308c1e429294f02d2090fffccab8e')
    jar.set('mojo-session-id', '{"id": "a3605148292ca1146ff7e4cb00e20998", "time": "1593280873412"}')
    jar.set('mojo-trace-id', '2')
    jar.set('Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2', '1593280888')
    jar.set('__mta', '144137482.1593276996539.1593280875437.1593280888469.3')
    jar.set('_lxsdk_s', '172f6f0c5d8-ba1-d7e-ec3%7C%7C4')
    return jar


def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    jar = prepare_cookie_jar()
    header = {'user-agent': user_agent}
    init_page = requests.get(myurl, headers=header, cookies=jar).text
    init_soup = bs(init_page, 'lxml')
    # selector of movie area: 'div.movies-list'
    movies_area = init_soup.find('div', attrs={'class': "movies-list"})
    movie_generator = (movie for movie in movies_area.find_all('dd'))
    # assign a list to give to pandas
    movie_data = {k: [] for k in ('name', 'genre', 'release-date')}
    for i in range(10):
        # movie name
        # selector of every movie title: div.channel-detail.movie-item-title > a
        current_movie = next(movie_generator)
        # current_movie_info contains:
        # 1. rating 2. genre 3. starring 4. release-time
        current_movie_info = current_movie.find('div', attrs={'class': 'movie-hover-info'})
        name = current_movie.find('div', attrs={'class': ['channel-detail', 'movie-item-title']}).find('a').text
        movie_data['name'].append(name)
        # movie genre
        # div.movie-item-hover > a > div > div:nth-child(2)
        genre = current_movie_info.find_all('div')[1].text.split(':', 1)[1].strip()
        movie_data['genre'].append(genre)
        # movie release date
        # div.movie-hover-title.movie-hover-brief
        release_date = current_movie_info.find_all('div')[3].text.split(':', 1)[1].strip()
        movie_data['release-date'].append(release_date)

    movie_dataFrame = pd.DataFrame(movie_data)
    movie_dataFrame.to_csv(f'./maoyan.csv', encoding='utf8', index=False, header=True)


@log_execution_time
def main(url):
    get_url_name(url)


main('https://maoyan.com/films?showType=3')
