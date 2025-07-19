import pymongo

CLIENT_CONNECTION_STRING = pymongo.MongoClient("mongodb://mongodb:27017/")

# Return a list of each of our databases within our MongoDB database.
def get_databases_from_mongodb_database():
    # Get a list of our database names.
    dataToReturn = CLIENT_CONNECTION_STRING().list_database_names()

    # Remove the 'default' databases from the list.
    dataToReturn.pop("admin", None)
    dataToReturn.pop("config", None)
    dataToReturn.pop("local", None)

    # Return our data, if there is any.
    if(dataToReturn):
        return dataToReturn
    else:
        return []

# Return a list of each of our collections, from within our chosen database, from within our MongoDB database.
# I know this isn't named nicely, but it's named correctly in terms of what we're actually doing.
def get_collections_from_database_from_mongodb_database(database):
    # Configure our database connection to use our chosen database
    DATABASE = CLIENT_CONNECTION_STRING[database]

    # Find all of our collections, from within our chosen database.
    dataToReturn = DATABASE.list_collections()

    # Return our data, if there is any.
    if(dataToReturn):
        return dataToReturn
    else:
        return []

# Return all the data from a specific collection, from within our MongoDB database.
def get_data_from_collection(database, collection):
    # Configure our database connection to use our chosen database and collection.
    COL = CLIENT_CONNECTION_STRING[database][collection]

    # Find all of our documents within our chosen collection, from within our chosen database.
    dataToReturn = COL.find({})

    # Return our data, if there is any.
    if(dataToReturn):
        return dataToReturn
    else:
        return []