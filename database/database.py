from pymongo import MongoClient
DATABASE_URL='mongodb+srv://quockhoaitay:quoc1999@cluster0.ap92qy6.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(DATABASE_URL)
print('Connected to MongoDB Atlas...')
print(client)
db = client.Balance
userCollection = db.Users