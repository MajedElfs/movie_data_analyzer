"""
------------------------------------------------------------------------
Movie Class Definition
------------------------------------------------------------------------
Author: Majed Hadida
ID:     200436110
Email:  hadi6110@mylaurier.ca
__updated__ = "2021-01-17"
------------------------------------------------------------------------
"""

class Movie:
    """
    -------------------------------------------------------
    CONSTANTS
    -------------------------------------------------------
    """
    MIN_RATING = 0
    MAX_RATING = 10
    FIRST_YEAR = 1888
    GENRES = ("science fiction", "fantasy", "drama", "romance", "comedy", "zombie", "action", "historical", "horror", "war", "mystery")
    # Defines a range of valid integer genre codes:
    GENRE_CODES = range(len(GENRES))
    
    # Makes it so that in order to call this function, you would have to call the class Movie then the function...
    # So Movie.genres()
    @staticmethod
    def genres_menu():
        """
        -------------------------------------------------------
        Creates a string of Movie genres in the format:
        0 science fiction
        1 fantasy
        2 drama
          ...
        10 mystery
        Use: s = Movie.genres_menu()
        Use: print(Movie.genres_menu())
        -------------------------------------------------------
        Returns:
            string - A numbered string of Movie.genres
        """
        string = ""
        counter = 0
        print("Genres")
        for x in range(len(Movie.GENRES)):
            string += "{:>2} {:>}\n".format(counter,Movie.GENRES[x])
            counter += 1
        return string
    
    def __init__(self, title, year, director, rating, genres):
        """
        -------------------------------------------------------
        Initializes a Movie object
        Use: movie = Movie(title, year, director, rating, genres)
        -------------------------------------------------------
        Parameters:
            title - movie title (str)
            year - year of release (int)
            director - name of director (str)
            rating - rating of 1 - 10 from IMDB (float)
            genres - numbers representing movie genres_list (list of int)
        Returns:
            A new Movie object (Movie)
        -------------------------------------------------------
        """
        # Making sure the user is inputting valid information
        assert year >= Movie.FIRST_YEAR, "Movie year must be >= {}".format(Movie.FIRST_YEAR)
        assert rating is None or Movie.MIN_RATING <= rating <= Movie.MAX_RATING, "Movie ratings must be between {} and {}".format(Movie.MIN_RATING, Movie.MAX_RATING)
        assert genres is None or genres == [] or min(genres) in Movie.GENRE_CODES, "Invalid genre code {}".format(min(genres))
        assert genres is None or genres == [] or max(genres) in Movie.GENRE_CODES, "Invalid genre code {}".format(max(genres))
        
        self.title = title
        self.year = year
        self.director = director
        self.rating = rating
        self.genres = genres
        
    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of movie data.
        Use: print(movie)
        Use: print( "{}".format(movie))
        Use: string = str(movie)
        -------------------------------------------------------
        Returns:
            string - the formatted contents of movie (str)
        -------------------------------------------------------
        """
        # Generate the list of genres as a string.
        genres_list = self.genres_string()
        string = ""
        
        print("{:<10}{}".format("Title:",self.title))
        print("{:<10}{}".format("Year:",self.year))
        print("{:<10}{}".format("Director:",self.director))
        print("{:<10}{}".format("Rating:",self.rating))
        print("{:<10}{}".format("Genres:",genres_list))
        
        return string
        
    def __eq__(self, other):
        """
        -------------------------------------------------------
        Compares this movie against another movie for equality.
        Use: movie == other
        -------------------------------------------------------
        Parameters:
            other - other movie to compare to (Movie)
        Returns:
            result - True if title and year match, False otherwise (boolean)
        -------------------------------------------------------
        """
        result = (self.title.lower(), self.year) == (other.title.lower(), other.year)
        return result
    
    def __lt__(self, other):
        """
        -------------------------------------------------------
        Determines if this movie comes before another movie.
        Use: movie < other
        -------------------------------------------------------
        Parameters:
            other - movie to compare to (Movie)
        Returns:
            result - True if movie precedes other, False otherwise (boolean)
        -------------------------------------------------------
        """
        result = (self.title.lower(), self.year) < (other.title.lower(), other.year)
        return result
    
    def __le__(self, other):
        """
        -------------------------------------------------------
        Determines if this movie precedes or is or equal to another movie.
        Use: movie <= other
        -------------------------------------------------------
        Parameters:
            other - movie to compare to (Movie)
        Returns:
            result - True if this movie precedes or is equal to other,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        result = self < other or self == other
        return result
    
    def genres_string(self):
        """
        -------------------------------------------------------
        Returns comma delimited string of genres based upon the
        current movie object's integer genres list.
        e.g.: [0, 2] returns "science fiction, drama"
        Use: string = movie.genres_string()
        -------------------------------------------------------
        Returns:
            string - string of genres (str)
        -------------------------------------------------------
        """
        string = ""
        if self.genres != None:
            for x in self.genres:
                if x == self.genres[-1]:
                    string += "{}".format(Movie.GENRES[x])
                else:
                    string += "{}, ".format(Movie.GENRES[x]) 
        else:
            string = None
        return string
        
    def genres_list_string(self):
        """
        -------------------------------------------------------
        Returns comma delimited string of genre indexes based upon the
        current movie object's integer genres list.
        e.g.: [0, 2] returns "0,2"
        Use: string = movie.genres_list_string()
        -------------------------------------------------------
        Returns:
            string - string of genre indexes (str)
        -------------------------------------------------------
        """
        string = ""
        for x in range(len(self.genres)):
            if x == len(self.genres)-1:
                string += "{}".format(self.genres[x])
            else:
                string += "{},".format(self.genres[x]) 
        return string
        
    def write(self, fv):
        """
        -------------------------------------------------------
        Writes a single line of movie data to an open file fv
        in the format
              title|year|director|rating|code
        Use: movie.write(fv)
        -------------------------------------------------------
        Parameters:
            fv - an already open file of movie data (file)
        Returns:
            None
        -------------------------------------------------------
        """
        fv. write("{}|{}|{}|{}|{}".format(self.title, self.year, self.director, self.rating, self.genres_list_string()))
        return 
    