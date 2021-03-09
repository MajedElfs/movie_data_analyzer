"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Majed Hadida
ID:     200436110
Email:  hadi6110@mylaurier.ca
__updated__ = "2021-01-17"
------------------------------------------------------------------------
"""
from Movie import Movie


def get_movie():
    """
    -------------------------------------------------------
    Creates a Movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Returns:
        movie - a Movie object based upon the user input (Movie).
    -------------------------------------------------------
    """
    title = input("Title: ")
    year = int(input("Year of release: "))
    director = input("Director: ")
    rating = float(input("Rating: "))
    genres = read_genres()
    movie = Movie(title, year, director, rating, genres)
    
    return movie


def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Returns:
        movie - a Movie object based upon the data from line (Movie)
    -------------------------------------------------------
    """
    # Makes a new list to seperate the information
    new_list = line.split("|")
    # Assigns each attribute to each part of the list
    title =  new_list[0]
    year = int( new_list[1])
    director =  new_list[2]
    rating = float( new_list[3])
    # Splits the genre numbers into a list so we can convert them into ints
    genres_temp = new_list[4].split(",")
    genres = []
    for x in genres_temp:
        genres.append(int(x))

    
    movie = Movie(title, year, director, rating, genres)
    return movie


def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of string data into a list of Movie objects.
    Use: movies = read_movies(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
    Returns:
        movies - a list of Movie objects (list of Movie)
    -------------------------------------------------------
    """
    movies = []
    for line in fv:
        movies.append(read_movie(line))
    return movies


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Returns:
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """
    print(Movie.genres_menu())
    genres = []
    user_input = None
    looping = True
    while looping:
        # Gets first number
        user_input = input("Enter a genre number (ENTER to quit): ")
        # Is the number they typed in NOT a number?
        if user_input.isalpha():
            print("Error: not a positive number.")
        # Is the input empty and the list is not empty?
        elif user_input == "" and len(genres) > 0:
            looping = False
        # If input is not empty... Make sure they typed in a numb between the range
        elif user_input != "":
            if int(user_input) > len(Movie.GENRES) or int(user_input) < 0:
                print("Error: input must be < {} and > 0".format(len(Movie.GENRES)))
            # Finally, check if the number isn't already in the list, then append it.
            elif int(user_input) not in genres:
                genres.append(int(user_input))

    genres.sort()
    return genres


def write_movies(fv, movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file of Movie objects converted to strings.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Returns:
        None
    -------------------------------------------------------
    """
    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of Movies from a particular year.
    The original list of movies must be unchanged.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Returns:
        ymovies - Movie objects whose year attribute is
            year (list of Movie)
    -------------------------------------------------------
    """

    ymovies = []
    for x in movies:
        if x.year == year:
            ymovies.append(x)

    return ymovies


def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of Movies whose ratings are equal to or higher
    than rating.
    The original list of movies must be unchanged.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Returns:
        rmovies - Movie objects whose rating attribute is
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """
    rmovies = []
    for x in movies:
        if x.rating >= rating:
            rmovies.append(x)
    return rmovies


def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include genre.
    The original list of movies must be unchanged.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Returns:
        gmovies - Movie objects whose genre list includes
            genre (list of Movie)
    -------------------------------------------------------
    """
    gmovies = []
    for x in movies:
        if genre in x.genres:
            gmovies.append(x)
    return gmovies


def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include all the genre
    codes in genres.
    The original list of movies must be unchanged.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Returns:
        gmovies - Movie objects whose genre list includes
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """
    gmovies = []
    for x in movies:
        if x.genres == genres:
            gmovies.append(x)

    return gmovies


def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    The original list of movies must be unchanged.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
    Returns:
        counts - the number of Movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """
    counts = []
    for c in range(len(Movie.GENRES)):
        counts.append(0)
    
    for x in movies:
        for y in x.genres:
            counts[y] += 1

    return counts



