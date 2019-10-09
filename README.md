Bmat TV/AV File API
===================

The purpose of this API is to provide an easy, fast and scalable file upload system. It is based on an rest API at
https://av-upload.bmat.com/doc/

Basic concepts
--------------
Every customer have, at least, one *namespace*. A namespaces is something like your username, a place where you can work
with your files in a completely isolated way. Like your *cloud hard disk*.

To ensure that only you can manage these files, you also need a *token*. This token is like a password and its very
important to keep it in a very safe place.

Every request you do (upload, list, remove and download a file) should contain these two value (namespace and toke).
Otherwise you will get a *Permission denied* error.

How to use it
-------------
Install `pip install file_api`

```python
import datetime
from file_api import Client

# For you production environment, please replace the namespace and token information to yours
c = Client(
    namespace="my-namespace",
    token="my-secret-token"
)

# Lets create a file
with open("myfile", "w") as f:
    f.write("Now is " + str(datetime.datetime.now()))

# Upload a file
file_id = c.put(open("myfile"))
# You will get an unique id that identifies this file
print("File uploaded with id", file_id)

# We can retrieve the file metadata like creation date, history of this file, the filename...
file_metadata = c.get(file_id)
print("File meatadata", file_metadata)

# You can also download the file contents
file_content = c.download(file_id)
print(file_content)

# Or list the files in your namespace
files = c.list()
# With pagination if you need it
files = c.list(page=3, page_size=15)

# And of course, you can remove the file
c.delete(file_id)
```

Check the file *example.py* to get the full example.
