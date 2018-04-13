import webbrowser


class Movie():
    """Class describing attributes an behavior of a Movie.

    Args:
        movie_title (str): Movie's title.
        movie_storyline (str): Movie's storyline.
        poster_image (str): Movie's poster image url.
        trailer_youtuebe (str): Movie's trailer youtube url.

    Attributes:
        title (str): Movie's title.
        storyline (str): Movie's storyline.
        poster_image_url (str): Movie's poster image url.
        trailer_youtube_url (str): Movie's trailer youtube url.

    Methods:
        show_trailer (): Show movie's trailer on a web browser
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Show current movie's trailer on a web brower

        Args:
            None.

        Returns:
            None.
        """
        webbrowser.open(self.trailer_youtube_url)
