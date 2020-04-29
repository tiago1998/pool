
import os

#
def cat_split(filename) :

	if not os.path.isfile(filename) :
	    raise Exception("[-] file "+filename+" not found")

	tmp = open(filename, "r")
	ret = tmp.read().split('\n')
	tmp.close()
        del ret[-1]
	return ret





def save_list(filename, lst) :
	
	f = open(filename, "w")
	f.write("\n".join(lst)+"\n")
	f.flush()
	f.close()
