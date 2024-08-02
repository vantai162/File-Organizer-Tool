import os
import shutil   #thu vien giup chinh sua folder, file 

path = input("Nhap vao folder can sap xep: ")
files = os.listdir(path)  #Lay danh sach cac file trong folder bo vao list

for target in files:
    filename,extension = os.path.splitext(target) #tach rieng ten file va extension ra
    extension = extension[1:]
    if os.path.exists(path + '/' + extension):  #neu folder da ton tai thi move file vao folder co duoi tuong ung
        shutil.move(path + '/' + target, path + '/' + extension)
    else:
        os.makedirs(path + '/' + extension)  #neu chua co thi tao
        shutil.move(path + '/' + target, path + '/' + extension)