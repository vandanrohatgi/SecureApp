from pymongo import MongoClient
from werkzeug.security import generate_password_hash


class database():
    def __init__(self):
        with open("connectionString.txt",'r') as f:
            data=f.read()
        ConnectionString=data
        client=MongoClient(ConnectionString)
        db=client['SecureApp']
        self.collection=db['credentials']
        '''initialCreds=[
            {"_id":1,"username":"admin","password":generate_password_hash("admin")},
            {"_id":2,"username":"user","password":generate_password_hash("user")}
            ]
        self.collection.insert_many(initialCreds)'''

    def query(self,username):
        item=self.collection.find_one({"username":username})
        return item

    #def updateData(self,user):
        
    def register(user,password,self):
        pass

#obj=database()
#print(obj.query("admin"))