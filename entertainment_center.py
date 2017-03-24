import fresh_tomatoes
import media



the_shawshank_redemption = media.Movie('The Shawshank Redemption',
        'https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg',
        'https://www.youtube.com/watch?v=6hB3S9bIaco',
        'Frank Darabont')

the_godfather = media.Movie('The Godfather',
        'https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg',
        'https://www.youtube.com/watch?v=sY1S34973zA',
        'Francis Ford Coppola')

the_dark_knight = media.Movie('The Dark Knight',
        'https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg',
        'https://www.youtube.com/watch?v=EXeTwQWrcwY',
        'Christopher Nolan')

movies = [the_shawshank_redemption, the_godfather, the_dark_knight]

fresh_tomatoes.open_movies_page(movies)
