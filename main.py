import pymongo
import time

s=['18.188.115.191:27017', '18.221.219.25:27017','18.191.172.47:27017']

client = pymongo.MongoClient('mongodb://172.31.19.92:27017,172.31.31.55:27017,172.31.30.13:27017/?replicaSet=rs0')

db = client["chat_db"]

col = db["chat"]


name = input('Input your nickname: ')


print('------------------------------------')
print('----------------CHAT----------------')
print('------------------------------------')
for i in col.find():
	print(i["name"]+": "+i["msg"])
print('------------------------------------')


while True:
	msg = input('new message: ')
	if msg == 'exit':
		break


	mydict = { "name": name, "msg": msg }

	x = col.insert_one(mydict)

	print('------------------------------------')
	print('----------------CHAT----------------')
	print('------------------------------------')
	for i in col.find():
		print(i["name"]+": "+i["msg"])
	print('------------------------------------')

