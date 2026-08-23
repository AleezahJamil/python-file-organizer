import os
import shutil
file_path="Write Folder path here"
files=os.listdir(file_path)
destination=os.path.join(file_path, "Codes")
destination2=os.path.join(file_path, "Images")
destination3=os.path.join(file_path, "Doc")

os.makedirs(destination,exist_ok=True)
os.makedirs(destination2,exist_ok=True)
os.makedirs(destination3,exist_ok=True)
for file in files:
    source=os.path.join(file_path,file)

    ext=os.path.splitext(file)
    file_name=ext[0]
    file_extention=ext[1]
    print("File name is: ", file_name)
    print("File type is: ",file_extention)
    if file_extention == ".py":
        dust=shutil.move(source,destination)
        print("Its Code! ",dust)

    elif file_extention in (".png" ,".jpg"):
        dust=shutil.move(source,destination2)

        print("Its Image! ",dust)
    elif file_extention in (".txt" , ".md"):
        dust=shutil.move(source,destination3)

        print("Its Docs! ",dust)
    else:
        print("Don't Know! ")


