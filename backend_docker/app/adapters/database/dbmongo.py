from pymongo import MongoClient

# variables
#URL_MONGO =  'mongodb://localhost:27017/' # only when you need logalhost
URL_MONGO =  'mongodb://db:27017/' # only when you need docker
MONGO_DB = 'state_company'

# Connection to the database
client = MongoClient(URL_MONGO)
conn = client[MONGO_DB]



