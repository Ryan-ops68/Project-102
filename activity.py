import cv2
import dropbox
import time
import random
starttime = time.time()
def takesnapshot():
    number = random.randint(0,200)
    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame  = videocaptureobject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        starttime = time.time
        result = False
        return img_name
    print("snapshot taken")
    videocaptureobject.release()
    cv2.destroyAllWindows()
def uploadimage(name):
    access_token = "sl.A3Py3jT4QORajpA7UmAh6acntj_OEcYu0IpulBQ5gRmQ_2kEG0nzMhi6HD2uP6tsjai5m2Dw7xsf2uQCekqLXL0IvXpqVJTL_4Ojl_EQjB4VI9FqPmlP0RmULBfD4USLnX-m-DXGe7A"
    file = name
    file_from = file
    file_to = "/pro/"+(name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")
def main():
    while(True):
        if ((time.time()-starttime)>=60):
            name = takesnapshot()
            uploadimage(name)
main()