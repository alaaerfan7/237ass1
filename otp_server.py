
# import library
import math, random

import socket
s = socket.socket() 

port = 6969

s.bind(('',port))
print ("socket binded to %s" %(port))

s.listen(5)
print ("socket is listening ")



username=input('please enter your username')
while username!= "alaaerfan":
    username=input("please input the correct username to have access ")
password=input('please enter your password')
while password!="1234":
    password=input("please input the correct password to access ")

# import library
import math, random

# function to generate OTP
def generateOTP() :

	# Declare a digits variable
	# which stores all digits
	digits = "0123456789"
	OTP = ""

# length of password can be changed
# by changing value in range
	for i in range(4) :
		OTP += digits[math.floor(random.random() * 10)]

	return OTP

# Driver code
if __name__ == "__main__" :
	
	print("OTP of 4 digits:", generateOTP())








while True:
    c, addr = s.accept()
    print ("got connection from ", addr)
    
    c.send("thank you for connecting".encode())
    
    c.close()
    
    break
