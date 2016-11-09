#import socket module
from socket import *

#choose a port from 1024 -> 65535 to listen on and
#assign to variable serverPort
#--TODO--

#Create TCP welcoming socket
#Notice the use of SOCK_STREAM for TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

#Bind the port and prepare the socket to
#listen for client requests (maximum 1)
#--TODO--

#Server is ready for requests
print 'Server is listening for requests...'

while True:
    #Request received, do three-way handshake,
    #and make a new connectionSocket
    #--TODO--
    
    try:
        #Fetch the message from the socket (use 1024 bytes buffer size)
        #--TODO--

        #---Start of Parsing HTTP request (Do not edit this section) ---
        #Extract the path of the requested object from the message
        #Path is second part of the HTTP header, identified by [1]
        filename = message.split()[1]
		
        #Because the extracted path of the HTTP request includes a
        # '\' character, we read the path from the second character
        f = open(filename[1:])
		
        #store the entire content of the requested file in a
        #temporary buffer
        outputdata = f.read()
        #--------------- End of Parsing HTTP request --------------------
		
        #Send the proper HTTP response header line to the connectionSocket
        #--TODO--
		
        #Send the content of the requested file
        #to the connectionSocket
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.send("\r\n")
		
        #close the connectionSocket to this client
        #--TODO--

    except IOError:
        #Problem fetching the file
        #Send a proper HTTP response message:
        #a) Send proper status code and phrase in header
        #b) Send html page with '404 File Not Found'
        #--TODO--

        #close the connectionSocket to this client
        #--TODO--
