ans = input("File name: ")

name, extension = ans.split(".")

file_types = {
    "gif": "image/gif",
    "jpg": "image/jpg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "document/pdf",
    "txt": "document/txt",
    "zip": "compressed/zip",
}

if extension in file_types:
    print(file_types[extension])
else:
    print("application / octet - stream")
