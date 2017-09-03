from movie import Movie

# 1
class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    # 2
    def __repr__(self):
        return "<User {}>".format(self.name)
    # 4
    def add_movie(self, name, genre):
        movie = Movie(name, genre, False)
        self.movies.append(movie)
    # 4
    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))

    # 3
    def watched_movies(self):
# It can be written two ways
        # Make an empty list
        # Iterate through self.movies
        # Add only the movie to the empty list only if it has been watched
# As below
        # watched_movies_list = []
        #
        # for movie in self.movies:
        #     if movie.watched:
        #         watched_movies_list.append(movie)
        # return watched_movies_list
# Or we can use filter method to do the same thing as below

        return list(filter(lambda x: x.watched, self.movies))

    #4
    def save_to_file(self):
        with open("{}.txt".format(self.name), 'w') as f:
            f.write(self.name + "\n")
            for movie in self.movies:
                f.write("{}, {}, {}\n".format(movie.name, movie.genre, str(movie.watched)))

    @classmethod
    def load_from_file(cls, file_name):
        with open(file_name, 'r') as f:
            content = f.readlines()
            username = content[0]
            movies = []
            for line in content[1:]:
                movie_data = line.split(",") # ["movie", "genre", True/False]
                movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == "True"))

            user = cls(username)
            user.movies = movies
            return user