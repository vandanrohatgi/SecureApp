from cryptography.fernet import Fernet

key=Fernet.generate_key()
obj=Fernet(key)

with open("key.key","wb") as f:
    f.write(key)

with open("database.txt","r") as f:
    data=f.read()

encrypted_data=obj.encrypt(data.encode())

with open("database.txt","wb") as f:
    f.write(encrypted_data)

def decrypt(filename):
    with open("key.key","rb") as f:
        key=f.read()
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    print(encrypted_data)
    decrypted_data = obj.decrypt(encrypted_data)
    # write the original file
    print(decrypted_data.decode())
    return(decrypted_data.decode())
