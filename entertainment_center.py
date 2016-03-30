import media
import fresh_tomatoes


toy_story = media.Movie("Toy Story",
                        "A story of a boy and and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

the_dark_knight = media.Movie("The Dark Knight",
                              "Joker wreaks havoc and chaos on the people of Gotham",
                              "http://juragan21.com/wp-content/uploads/2015/08/The-Dark-Knight.jpg",
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY")

movies = [toy_story, the_dark_knight]
fresh_tomatoes.open_movies_page(movies)
