from database import Database
from models.post import Post 

Database.initialize()

post = Post.from_mongo("cc6bc2c95d714781acad21827d1011e7",)


print(post)