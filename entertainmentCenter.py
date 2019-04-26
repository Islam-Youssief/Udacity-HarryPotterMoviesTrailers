"""
This file is about Adding the whole trailer series of Harry Potter
Every film includes the name of the film and year of release
Every film has a short description
Every film has a poster showing the actors
Every film has it's trailer.
Names of the movies :-
    Harry Potter and the Philosopher's Stone (2001)
    Harry Potter and the Chamber of Secrets (2002)
    Harry Potter and the Prisoner of Azkaban (2004)
    Harry Potter and the Goblet of Fire (2005)
    Harry Potter and the Order of the Phoenix (2007)
    Harry Potter and the Half-Blood Prince (2009)
    Harry Potter and the Deathly Hallows – Part 1 (2010)
    Harry Potter and the Deathly Hallows – Part 2 (2011)
    Fantastic Beasts and Where to Find Them.
"""
import media
import HarrySeries

# Adding Harry Potter and the Philosopher's Stone (2001)
HarryPotter1 = media.Movie(
    "The Philosopher's Stone(2001)",
    "First film of Harry Potter and the Philosopher's Stone (2001).",
    "http://static.rogerebert.com/uploads/movie/movie_poster/harry-potter-and-"
    .strip() + "the-sorcerers-stone-2001/"
    .strip() + "large_uLGaJ9FgPWf7EUgwjp9RTmHemw8.jpg",
    "https://www.youtube.com/watch?v=ACNzq06azSw")

# Harry Potter and the Chamber of Secrets (2002)
HarryPotter2 = media.Movie(
    "The Chamber of Secrets (2002)",
    "Harry ignores warnings not to return to Hogwarts, only to find the school\
    plagued by a series of attacks and a strange voice haunting him.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTcx"
    .strip() + "ODgwMDkxNV5BMl5BanBnXkFtZTYwMDk2MDg3._V1_.jpg",
    "https://www.youtube.com/watch?v=YzJ93X5fNp8")

# Harry Potter and the Prisoner of Azkaban (2004)
HarryPotter3 = media.Movie(
    "The Prisoner of Azkaban (2004)",
    "It's Harry's third year at Hogwarts not only does he have a new\
    \"Defense Against the Dark Arts\"teacher,but also trouble brewing",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY4NTIwODg0N15BMl5B"
    .strip() + "anBnXkFtZTcwOTc0MjEzMw@@._V1_SY1000_CR0,0,676,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=lAxgztbYDbs")

# Harry Potter and the Goblet of Fire (2005)
HarryPotter4 = media.Movie(
    "The Goblet of Fire (2005)",
    "Harry finds himself mysteriously selected as an under-aged competitor\
    in a dangerous tournament between three schools of magic.",
    "https://upload.wikimedia.org/wikipedia/ar/thumb/0/08"
    .strip() + "/GoFposter.jpg/223px-GoFposter.jpg",
    "https://www.youtube.com/watch?v=7IDKCAD_GDw")

# Harry Potter and the Order of the Phoenix (2007)
HarryPotter5 = media.Movie(
    "The Order of the Phoenix (2007)",
    "With their warning about Lord Voldemort's return scoffed at,\
    Harry and Dumbledore are targeted. ",
    "https://images-na.ssl-images-amazon.com/images/"
    .strip() + "M/MV5BMTM0NTczMTUzOV5BMl5BanBnXkFtZTYwMzIxNTg3._V1_.jpg",
    "https://www.youtube.com/watch?v=7mRmJ1ZBZs0")

# Harry Potter and the Half-Blood Prince (2009)
HarryPotter6 = media.Movie(
    "The Half-Blood Prince (2009)",
    "As Harry Potter begins his sixth year at Hogwarts, he discovers an old\
    book marked as \"the property of the Half-Blood Prince\"\
    and begins to learn more.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNzU3NDg4NTAyNV5BM"
    .strip() + "l5BanBnXkFtZTcwOTg2ODg1Mg@@._V1_SY1000_CR0,0,648,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=jpCPvHJ6p90")

# Harry Potter and the Deathly Hallows – Part 1 (2010)
HarryPotter7 = media.Movie(
    "The Deathly Hallows (2010)",
    "As Harry races against time and evil to destroy the Horcruxes, he uncovers\
    the existence of three most powerful objects in the wizarding world.",
    "https://upload.wikimedia.org/wikipedia/ar/3/31/HP7part1poster.jpg",
    "https://www.youtube.com/watch?v=MxqsmsA8y5k")

# Harry Potter and the Deathly Hallows – Part 2 (2011)
HarryPotter8 = media.Movie(
    "The Deathly Hallows (2011)",
    "Harry, Ron and Hermione search for Voldemort's remaining Horcruxes\
    in their effort to destroy the Dark Lord as the final battle\
    rages on at Hogwarts.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY2MTk3MDQ1N15BMl5"
    .strip() + "BanBnXkFtZTcwMzI4NzA2NQ@@._V1_SY1000_SX675_AL_.jpg",
    "https://www.youtube.com/watch?v=I_kDb-pRCds")

# Fantastic Beasts and Where to Find Them
FantasitcBeast = media.Movie(
    'Fantastic Beasts and Where to Find',
    "The adventures of writer Newt Scamander in New York's secret community\
    of witches and wizards.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMxOTM1OTI4MV5BMl5B"
    .strip() + "anBnXkFtZTgwODE5OTYxMDI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=Vso5o11LuGU")

# Adding all the movies in order
movies = [
    HarryPotter1, HarryPotter2, HarryPotter3,
    HarryPotter4, HarryPotter5, HarryPotter6,
    HarryPotter7, HarryPotter8, FantasitcBeast]
# opening the page with movies
HarrySeries.open_movies_page(movies)
