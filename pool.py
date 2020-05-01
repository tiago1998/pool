#!/usr/bin/python2


import sys
if len(sys.argv) != 4:
	print("use mode:\n\t"+sys.argv[0]+" port list-steps key")
	sys.exit(127)


import socket, time
import threading

sys.path.append("./modules")
import loaders
import data
import auth
import data
import step 
import link


#
def answerClient(client, clientaddr) :
		
    if not auth.auth(client) :
        client.send("wrong key")
	client.close()
        return 0
    client.send(str("ok"))

    while True:
        req=client.recv(1024)
        if req.startswith("link") :
            client.send(link.link())
        elif req.startswith("appendLink") :
            client.send(link.append(req))
        elif req.startswith("getStep") :
            client.send(step.checkStep(req))
        else :
            client.close()
            break
    return 1



#
def main() :

        print ("loading")
        loaders.loadData()

	print ("[*] loading links")
	sys.stdout.flush()
	loaders.loadLinks(data.filename_steps)
	print ("[+] "+str(len(data.list_links))+" links loaded\n[*] loading steps")
	sys.stdout.flush()
        loaders.loadSteps(data.filename_steps)
        print ("[+] "+str(len(data.list_steps))+" steps loaded")
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(("0.0.0.0", int(data.port)))
	sock.listen(1024)
	print ("\n\t[...] listening on 0.0.0.0:"+str(data.port))
	sys.stdout.flush()

	while True :
		(client, clientaddr) = sock.accept()
		t = threading.Thread(target=answerClient, args=(client, clientaddr))
		t.start()
		time.sleep(1)

	sock.close()


if __name__ == '__main__' :
	main()
