class Show:
    """
    The show class, each instance will correspond to a show
    """
    def __init__(self, res):
        self.id = res['id']
        self.title = res['name']
        self.date = res['first_air_date']
        self.popularity = res['popularity']
        self.vote_average = res['vote_average']
        self.poster_path = res['poster_path']
        self.overview = res['overview']


class ShowDetailedView(Show):

    def __init__(self, res):
        Show.__init__(self, res)
        self.origin_country = res['origin_country'][0]
        self.film_maker = res['created_by'][0]['name']
        self.production_company = res['production_companies'][0]['name']
        self.genres = res['genres'][0]['name']
        self.number_of_seasons = res['number_of_seasons']
        self.number_of_episodes = res['number_of_episodes']
        self.season = []
        self.next_episode_to_air = Episode(self.id, res['next_episode_to_air']['season_number'],
                                           res['next_episode_to_air']['episode_number'])

        for i in range(self.number_of_seasons + 1):
            self.season.append(Season(res['season'][i]['id']))


class Season:

    def __init__(self, season_id):
        self.id = season_id


class Episode:

    def __init__(self, show_id, season_number, episode_number):
        self.show_id = show_id
        self.season_number = season_number
        self.episode_number = episode_number


"""
Now if you want complete freedom of adding more parameters:

class Cheese():
    def __init__(self, *args, **kwargs):
        #args -- tuple of anonymous arguments
        #kwargs -- dictionary of named arguments
        self.num_holes = kwargs.get('num_holes',random_holes())

Here is the list that needs to be completed of parameters for a show_quick_view (-- : ignore) :
poster_path
popularity
id
--backdrop_path
vote_average
overview
first_air_date
--origin_country
--genre_ids
--original_language
vote_count
name
--original_name
"""