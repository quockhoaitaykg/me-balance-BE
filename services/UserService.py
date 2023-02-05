from models.Users import UsersBaseModel
from database import database

async def fetch_one_user(title):
    document = await database.userCollection.find_one({"title": title})
    return document

async def fetch_all_users():
    users = []
    cursor = database.userCollection.find({})
    for document in cursor:
        users.append(UsersBaseModel(**document))
    return users

async def create_user(user):
    document = user
    result = await database.userCollection.insert_one(document)
    return document


# async def update_todo(title, desc):
#     await collection.update_one({"title": title}, {"$set": {"description": desc}})
#     document = await collection.find_one({"title": title})
#     return document
#
# async def remove_todo(title):
#     await collection.delete_one({"title": title})
#     return True