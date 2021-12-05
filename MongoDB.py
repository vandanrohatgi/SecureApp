from pymongo import MongoClient
from werkzeug.security import check_password_hash, generate_password_hash


class database():
    def __init__(self):
        with open("connectionString.txt",'r') as f:
            ConnectionString=f.read()
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

    def updateData(self,oldName=None,newName=None,oldPassword=None,newPassword=None):
        if newName and self.query(oldName):
            try:
                self.collection.update_one(filter={'username':oldName},update={"$set":{'username':newName}})
            except:
                raise "Error while updating database"
        if oldPassword:
            try:
                current=self.query(oldName)['password']
                correct=check_password_hash(current,generate_password_hash(oldPassword))
                if correct:
                    self.collection.update_one(filter={'username':oldName},update={"$set":{'password':generate_password_hash(newPassword)}})
                else:
                    raise Exception
            except:
                raise "Error while updating database"
   
    def register(user,password,self):
        pass

obj=database()
print(obj.query("adin"))