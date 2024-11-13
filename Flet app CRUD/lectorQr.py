import flet as ft
from flet import *
# INSTALL YOU OPENCV WITH PIP
import numpy as np
import cv2
 
def main(page:Page):
 
	myresult = Column()
 
	def readqrcode(e):
		cap = cv2.VideoCapture(0)
		while True:
			ret,frame = cap.read()
			if not ret:
				break
 
			gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
			detector = cv2.QRCodeDetector()
			data,points,_ = detector.detectAndDecode(gray)
 
			# AND IF THE OPENCV FOUND YOU QR CODE AND GET TEXT FROM QRCODE
			if data:
				cv2.polylines(frame,[np.int32(points)],True,(255,0,0),2,cv2.LINE_AA)
				print(f"QR Code YOu Data is : {data}")
 
				# AND PUSH TO TEXT WIDGET IF FOUND 
 
				myresult.controls.append(
					Text(data,size=25,weight="bold")
					)
				page.update()
 
				cap.release()
				# AND CLOSE WINDOW WEBCAM IF FOUND TEXT FROM QRCODE
				cv2.destroyAllWindows()
				break
 
				# AND IF YOU PRESS q IN WEBCAM WINDOW THEN CLOSE THE WEBCAM
			cv2.imshow("QR CODE DETECTion ",frame)
			if cv2.waitKey(1) & 0xFF == ord("q"):
				break
				# STOP YOU WINDOW
		if cap.isOpened():
			cap.release()
			cv2.destroyAllWindows()
 
 
	page.add(
	Column([
        Text("Read Qrcode from You Phone",size=30,weight="bold"),
        ElevatedButton("Read Qr Code",
            bgcolor="blue",color="white",
            on_click=readqrcode
        ),
        # AND SHOW RESULT FROM YOU QR CODE TO TEXT WIDGET
        Text("Result qr code",size=20,weight="bold"),
        Divider(),
        myresult
    
    
        ])
    
	)
 
ft.app(target=main)