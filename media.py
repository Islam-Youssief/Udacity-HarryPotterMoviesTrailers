import webbrowser

"""  This module contains
the initialization.  """


class Movie ():
    """This class contains the initializations
    show trailer function
    show poster image.
    """

# constructor of every movie
    def __init__(
                self, movieTitle, movieStoryLine, posterImage, trailerYoutube):
        self.title = movieTitle
        self.movieStoryLine = movieStoryLine
        self.poster_image_url = posterImage
        self.trailer_youtube_url = trailerYoutube

# This method is created to show the trailer of the movie specified
    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)

# This method is created to show the poster image of the movie specified
    def showPosterImage(self):
        webbrowser.open(self.poster_image_url)
