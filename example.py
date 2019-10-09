# Run pip install file_api to get the library
from file_api import Client
import datetime

namespace = "my-namespace"
token = "my-access-token"

c = Client(
    namespace=namespace,
    token=token
)


with open("myfile", "w") as f:
    f.write("Now is " + str(datetime.datetime.now()))

file_id = c.put(open("myfile"))
print("File uploaded with id", file_id)

files = c.list()
print("Uploaded files ({total})".format(total=files["total"]))
for i in files["data"]:
    print(i["path"])
file_id = files["data"][0]["id"]
file_info = c.get(file_id)
file_content = c.download(file_id)
print("The file content is:", file_content)
if c.delete(file_id):
    print("File deleted")
else:
    print("File could not be deleted, you may not have permissions or file does not exist")