name_of_file = input("File name: ").strip().lower()

if name_of_file.endswith(".gif"):
    print("image/gif")
elif name_of_file.endswith(".jpg"):
    print("image/jpeg")
elif name_of_file.endswith(".jpeg"):
    print("image/jpeg")
elif name_of_file.endswith(".png"):
    print("image/png")
elif name_of_file.endswith(".pdf"):
    print("application/pdf")
elif name_of_file.endswith(".txt"):
    print("text/plain")
elif name_of_file.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
