class Show:
    """
    The show class, each instance will correspond to a show

    """
    def __init__(self, id, kind='id_only', **kwargs):
        self.__id = id
        
        # The kind attribute will help us know how complete is the show instance
        self.__kind = kind
        if not kwargs.get('name', False):
            self.__kind = kind
        elif not kwargs.get('status', False):
            self.__kind = 'quick_view'
        else:
            self.__kind = 'full_view'

        # These are the quick view attributes
        self.__name = kwargs.get('name', None)
        self.__vote_average = kwargs.get('vote_average', None)
        self.__vote_count = kwargs.get('vote_count', None)
        self.__overview = kwargs.get('overview', None)
        self.__first_air_date = kwargs.get('first_air_date', None)

        # These are the full view view attributes
        self.__seasons = kwargs.get('seasons', None)
        self.__next_episode_to_air = kwargs.get('next_episode_to_air', None)
        self.__created_by = kwargs.get('created_by', None)

    # Getters and setters for all the attributes
    def get_kind(self):
        return self.__kind

    def set_kind(self, kind):
        self.__kind = kind

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_vote_average(self):
            return self.__vote_average

    def set_vote_average(self, vote_average):
        self.__vote_average = vote_average

    def get_first_air_date(self):
            return self.__first_air_date

    def set_first_air_date(self, first_air_date):
        self.__first_air_date = first_air_date

    def get_overview(self):
            return self.__overview

    def set_overview(self, overview):
        self.__overview = overview

    def get_seasons(self):
        return self.__seasons

    def set_seasons(self, seasons):
        self.__seasons = seasons

    def get_next_episode_to_air(self):
        return self.__next_episode_to_air

    def set_next_episode_to_air(self, next_episode_to_air):
        self.__next_episode_to_air = next_episode_to_air

    def get_created_by(self):
        return self.__created_by

    def set_created_by(self, created_by):
        self.__created_by = created_by

    def get_vote_count(self):
        return self.__vote_count

    def set_vote_count(self, vote_count):
        self.__vote_count = vote_count





"""
Now if you want complete freedom of adding more parameters:

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