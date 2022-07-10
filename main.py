import pymongo

db_client = pymongo.MongoClient("mongodb://localhost:27017/")

current_db = db_client["mongo"]
collection = current_db["cars"]


hondacrv = {
    'title': 'Honda cr-v',
    'url': 'https://auto.honda.ru/crv/',
    'engine_power': '150'
}

ins_result = collection.insert_one(hondacrv)
print(ins_result.inserted_id)

cars = [
    {'title': 'Tesla Model 3', 'url': 'https://www.tesla.com/model3', 'engine_power': '450'},
    {'title': 'Honda Civic', 'url': 'https://auto.honda.ru/archival/civic-ix/civic-5d-ix/', 'engine_power': '141'},
    {'title': 'Ford F-150', 'url': 'https://www.ford.com/trucks/f150/', 'engine_power': '450'},
    {'title': 'Nissan Sylphy', 'url': 'https://www.nissan.ru/', 'engine_power': '105'}
]

ins_result = collection.insert_many(cars)
print(ins_result.inserted_ids)


for car in collection.find():
    print(car)







