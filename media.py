
class Movie(object):
    """
        title: Movie title.
        poster_image_url: URL to movie poster image.
        trailer_youtube_url: URL to movie trailer on YouTube.
        director: Movie director name.
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url, director):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.director = director
