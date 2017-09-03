from database import Database
from user import User

Database.initialise(user='postgres', password='chandu', database='learning', host='localhost', port='5433')

my_user = User('akshara@gmail.com', 'akshara', 'prasad', None)

my_user.save_to_db()

user_from_db = User.load_from_db_by_email('chandrasen91@gmail.com')

print(user_from_db)

my_user.save_to_db()