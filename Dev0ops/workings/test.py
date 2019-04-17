import pickle
import base64

X = {'Subject': 'Hello'}

with open("test.obj", "wb") as file:
    pickle.dump(X, file)

pickleStr = None
with open("test.obj", "rb") as file:
    pickleStr = file.read()

print("BASE64: ")
print(base64.b64encode(pickleStr).decode("utf-8"))

print("UNPICKLE TEST:")
postObj = pickle.loads(pickleStr)
print(postObj['Subject'])
