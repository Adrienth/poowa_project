import requests
params = {'api_key': '7ecd6a3ceec1b96921b4647095047e8e'}


class Show:
    """
    The show class, each instance will correspond to a show
    """

    def __init__(self, res):
        self._id = res['id']
        self._title = res['name']
        self._date = res['first_air_date'][:4]
        self._popularity = res['popularity']
        self._vote_average = res['vote_average']
        self._poster_path = res['poster_path']
        self._poster_url = None
        self._overview = res['overview']
        self._trunc_overview = None

    def _get_id(self):
        return self._id

    def _get_title(self):
        return self._title

    def _get_date(self):
        return self._date

    def _get_popularity(self):
        return self._popularity

    def _get_vote_average(self):
        return self._vote_average

    def _get_poster_path(self):
        return self._poster_path

    def _get_poster_url(self):
        if self._poster_path is None:
            return None
        else:
            return 'https://image.tmdb.org/t/p/w200' + self._poster_path

    def _get_overview(self):
        return self._overview

    def _get_trunc_overview(self):
        nb_char = 270
        view = self._overview
        if len(view) > nb_char:
            view = view[:nb_char] + '...'
        return view

    id = property(_get_id)
    title = property(_get_title)
    date = property(_get_date)
    popularity = property(_get_popularity)
    vote_average = property(_get_vote_average)
    poster_path = property(_get_poster_path)
    poster_url = property(_get_poster_url)
    overview = property(_get_overview)
    trunc_overview = property(_get_trunc_overview)


class ShowDetailedView(Show):

    def __init__(self, show_id):
        req = requests.get('https://api.themoviedb.org/3/tv/' + str(show_id), params)
        res = req.json()
        Show.__init__(self, res)
        self._origin_country = res['origin_country']
        self._film_maker = res['created_by']
        self._production_companies = res['production_companies']
        self._genres = res['genres']
        self._next_episode_to_air = res['next_episode_to_air']
        self._number_of_seasons = res['number_of_seasons']
        self._seasons = []
        i = 1
        while i <= self._number_of_seasons:
            self._seasons += [Season(self._id, i)]
            i += 1

    def _get_origin_country(self):
        return self._origin_country[0]

    def _get_film_maker(self):
        return self._film_maker[0]['name']

    def _get_production_companies(self):
        return self._production_companies[0]['name']

    def _get_genres(self):
        return self._genres[0]['name']

    def _get_next_episode_to_air(self):
        return self._next_episode_to_air

    def _get_number_of_seasons(self):
        return self._number_of_seasons

    def _get_seasons(self):
        return self._seasons

    origin_country = property(_get_origin_country)
    film_maker = property(_get_film_maker)
    production_companies = property(_get_production_companies)
    genres = property(_get_genres)
    next_episode_to_air = property(_get_next_episode_to_air)
    number_of_seasons = property(_get_number_of_seasons)
    seasons = property(_get_seasons)


class Season:

    def __init__(self, show_id, season_number, show_title=None):
        req = requests.get('https://api.themoviedb.org/3/tv/' + str(show_id) + '/season/' + str(season_number), params)
        res = req.json()
        self._show_title = show_title
        self._season_number = res['season_number']
        self._name = res['name']
        self._overview = res['overview']
        self._poster_path = res['poster_path']
        self._poster_url = None
        self._episode_count = len(res['episodes'])
        self._air_date = res['air_date'][:4]
        self._episodes = []
        for episode in res['episodes']:
            self._episodes += [Episode(episode)]

    def _get_show_title(self):
        return self._show_title

    def _get_season_number(self):
        return self._season_number

    def _get_name(self):
        return self._name

    def _get_overview(self):
        return self._overview

    def _get_trunc_overview(self):
        nb_char = 270
        view = self._overview
        if len(view) > nb_char:
            view = view[:nb_char] + '...'
        return view

    def _get_poster_path(self):
        return self._poster_path

    def _get_poster_url(self):
        if self._poster_path is None:
            return None
        else:
            return 'https://image.tmdb.org/t/p/w200' + self._poster_path

    def _get_episode_count(self):
        return self._episode_count

    def _get_air_date(self):
        return self._air_date

    def _get_episodes(self):
        return self._episodes

    show_title = property(_get_show_title)
    season_number = property(_get_season_number)
    name = property(_get_name)
    overview = property(_get_overview)
    trunc_overview = property(_get_trunc_overview)
    poster_path = property(_get_poster_path)
    poster_url = property(_get_poster_url)
    episode_count = property(_get_episode_count)
    air_date = property(_get_air_date)
    episodes = property(_get_episodes)


class Episode:

    def __init__(self, res):
        self._air_date = res['air_date']
        self._vote_average = int(res['vote_average']*10)/10
        self._name = res['name']
        self._poster_path = res['still_path']
        self._poster_url = None
        self._overview = res['overview']
        self._trunc_overview = None

    def _get_name(self):
        return self._name

    def _get_overview(self):
        return self._overview

    def _get_trunc_overview(self):
        nb_char = 270
        view = self._overview
        if len(view) > nb_char:
            view = view[:nb_char] + '...'
        return view

    def _get_poster_path(self):
        return self._poster_path

    def _get_poster_url(self):
        if self._poster_path is None:
            return None
        else:
            return 'https://image.tmdb.org/t/p/w300' + self._poster_path

    def _get_vote_average(self):
        return self._vote_average

    def _get_air_date(self):
        return self._air_date

    name = property(_get_name)
    overview = property(_get_overview)
    trunc_overview = property(_get_trunc_overview)
    poster_path = property(_get_poster_path)
    poster_url = property(_get_poster_url)
    air_date = property(_get_air_date)
    vote_average = property(_get_vote_average)

"""
class Cheese():
    def __init__(self, *args, **kwargs):
        #args -- tuple of anonymous arguments
        #kwargs -- dictionary of named arguments
        self.num_holes = kwargs.get('num_holes',random_holes())


Here is the list that needs to be completed of parameters for a show_quick_view (-- : we ignore) :
poster_path
popularity
id
vote_average
vote_count
overview
first_air_date
name
--backdrop_path
--original_name
--origin_country
--genre_ids
--original_language


Here is the list that needs to be completed of parameters for a show_full_view (-- : we ignore) :
poster_path
popularity
id
vote_average
vote_count
overview
first_air_date
name
seasons(
    air_date,
    episode_count,
    id,name,
    overview,
    poster_path,
    season_number)
next_episode_to_air(
    air_date,
    episode_number,
    id,name,
    overview,
    production_code,
    season_number,
    show_id,
    still_path,
    vote_average,
    vote_count)
created_by (
    id,
    credit_id,
    name,
    gender,
    profile_path)
status
--original_name
--origin_country
--genres(
    id,
    name)
--original_language
--backdrop_path
--episode_run_time
--homepage
--in_production
--languages
--last_air_date
--last_episode_to_air(
    air_date,
    episode_number,
    id,name,
    overview,
    production_code,
    season_number,
    show_id,
    still_path,
    vote_average,
    vote_count)

--networks(
    name,
    id,
    logo_path,
    origin_country)
--number_of_episodes
--number_of_seasons
--production_companies(
    id, 
    logo_path,
    name,
    origin_country)
--status
--kind
"""