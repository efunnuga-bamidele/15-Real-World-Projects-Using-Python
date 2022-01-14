#import module
import datetime
import pyqrcode

#Greetings
print("Welcome to QRcode generaotr tool")

#Request user message input to generate code

userMessage = input("Enter you message to be encrypted : ")
generatedCode = pyqrcode.create(userMessage)


# get created datestamp
currentDate = datetime.datetime.now()
timeStampFormatted = currentDate.strftime("%d-%b-%Y(%H-%M-%S-%f)")

# save as image
file_name = "QRcode_"+str(timeStampFormatted)+".png"
generatedCode.png(file_name, scale=5)
print("QRcode was generated successfully!")