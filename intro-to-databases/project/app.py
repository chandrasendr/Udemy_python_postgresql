from user import User

my_user = User('puppy.prasad@gmail.com', 'prasad', 'rajashekar', None)

my_user.save_to_db()

user_from_db = User.load_from_db_by_email('chandrasen91@gmail.com')

print(user_from_db)

my_user.save_to_db()