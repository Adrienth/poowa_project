class Show:
    """
    The show class, each instance will correspond to a show
    """
    def __init__(self, id, name=None):
        self.name = name
        self.id = i



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