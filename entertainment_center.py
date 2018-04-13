import media
# fresh tomatoes is a mudule from https://github.com/udacity/ud036_StarterCode
import fresh_tomatoes


#  Create some movie instantiation using Movie class in Module media
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toy that come to life",
                        "http://upload.wikimedia.org/wikipedia"
                        "/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                     "A marine on an aline planet",
                     "https://upload.wikimedia.org/wikipedia"
                     "/zh/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                       "A man escape from prison",
                                       "https://upload.wikimedia.org/wikipedia"
                                       "/en/8/81/ShawshankRedemptionMoviePoster.jpg",   # NOQA
                                       "https://www.youtube.com/watch"
                                       "?v=6hB3S9bIaco")
zootopia = media.Movie("Zootopia",
                       " A rabbit pliceman's story",
                       "https://upload.wikimedia.org/wikipedia"
                       "/en/e/ea/Zootopia.jpg",
                       "https://www.youtube.com/watch?v=jWM0ct-OLsM")
inception = media.Movie("Inception",
                        "A story about a professional thief"
                        "who steals information"
                        "by infiltrating the subconscious",
                        "https://upload.wikimedia.org/wikipedia"
                        "/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")
movies = [toy_story, avatar, the_shawshank_redemption, zootopia, inception]
fresh_tomatoes.open_movies_page(movies)   # Show movies on website
