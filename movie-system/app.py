from user import User

user = User.load_from_file('chandra.txt')

print(user.name)
print(user.movies)