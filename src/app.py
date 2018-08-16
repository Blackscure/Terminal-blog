from database import Database
from models.post import Post 

Database.initialize()

post = Post.from_mongo("77515483f72c46b8b3e873f3bd1312e3")


print(post)