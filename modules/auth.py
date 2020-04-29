import data



#
def auth(client) :

	req = client.recv(1024)
	if not req.find(data.key) > -1 :
	    return 0
	return 1
