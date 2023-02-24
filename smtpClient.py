from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # with smtplib can use something the following smtp_server = smtplib.SMTP(smtp_server, ####) but using the
    # following for now in terminal `python3 -m smtpd -c DebuggingServer -n 127.0.0.1:1025`

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    #like the tcp server but with mailserver
    clientSocket = socket(AF_INET,SOCK_STREAM )
    clientSocket.connect(mailserver)

    # Fill in start
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    # Fill in end
    mailOut = 'MAIL FROM <jessemoskowitz@nypl.org>\r\n'
    clientSocket.send(mailOut.encode()) # do I need to use that 'rb' type?? no right?
    recv2 = clientSocket.recv(1024).decode()

    # Send RCPT TO command and handle server response.
    # Fill in start
    readReceipt = "RCPT TO: <someoneatNYU@nyu.edu>\r\n"
    clientSocket.send(readReceipt.endcode())
    recv3 = clientSocket.recv(1024)
    # print('RR sent')
    # Fill in end

    # Send DATA command and handle server response.
    data = "DATA is everyones fav Star Trek character\r\n"
    clientSocket.send(readReceipt.endcode())
    recv4 = clientSocket.recv(1024)
    recv4 = recv4.decode()
    #print('HERE ________ after DATA sent/recvd')
    # Fill in start
    # Fill in end

    # Send message data.
    # Fill in start
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')