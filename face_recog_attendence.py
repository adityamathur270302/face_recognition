import face_recognition
import cv2

def login():
    print("\t\t   WELCOME TO LOGIN MANAGEMENT SYSTEM \n")
    print("\t\t PRESS 1 FOR EXIXTING USER\n")#if your face is already enrolled.
    print("\t\t PRESS 2 FOR NEW USER\n")
    try:
        o=int(input("Your choice-:"))
        if o==2:
            name=input("ENTER YOUR NAME-:")
            print("LOOK INTO THE WEBCAM... ")
            print("recognizing face.....")

    
            videoCaptureObject = cv2.VideoCapture(0)
            result = True
            while(result):
                ret,frame = videoCaptureObject.read()
                cv2.imwrite(name + ".jpg",frame)#your image will be saved by your name
                result = False
                videoCaptureObject.release()
                cv2.destroyAllWindows()
                print("YOU HAVE BEEN REGISTERED INTO THE ACCOUNT!!")
        elif o==1:
            name1=input("ENTER YOUR NAME-:")




            img1 = face_recognition.load_image_file(name1 +".jpg")
            videoCaptureObject = cv2.VideoCapture(0)
            result = True
            while(result):
                ret,frame = videoCaptureObject.read()
                cv2.imwrite("current.jpg",frame)#your image will be compared by the image whose name you entered.
                result = False
                videoCaptureObject.release()
                cv2.destroyAllWindows()
                                                   
                unknown_img = face_recognition.load_image_file("current.jpg")

                img_encoding = face_recognition.face_encodings(img1)[0]
                unknown_encoding = face_recognition.face_encodings(unknown_img)[0]
        
                results = face_recognition.compare_faces([img_encoding], unknown_encoding)#compare your current image with the entered image name.
                if results==[True]:
                    print("LOGGED IN SUCCESSFULY!!")
                elif results==[False]:
                    print("NO RCECORD FOUND!! TRY AGAIN!")
                else:
                    print("")
        else:
            print("TRY AGAIN")
        
    except:
        print("OPPS !! AN ERROR OCCURRED PLEASE TRY GAIN")
#this project is created by Aditya Mathur
