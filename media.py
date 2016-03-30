import webbrowser


""" This class stores movie information. """
class Movie:
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """ This is the constructor that takes multiple perameters
            the title, the story line, an image, and a link to
            youtube tailer. Able to create muliple instances."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ When method is called a youtube trailer opens"""
        webbrowser.open(self.trailer_youtube_url)
