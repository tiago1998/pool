
import sys
import filemanager
import data

def loadData() :
    global data

    data.port = sys.argv[1]
    data.filename_steps = sys.argv[2]
    data.key = sys.argv[3]



def stepToLink(s) :
    ret = []
    for line in s :
        ret.append(line.split(';')[0]);
    return ret


def printLinks() :
    global data
    for l in data.list_links :
        print "link: "+l


def loadLinks(filename_links) :
        global data
	data.list_links = stepToLink(filemanager.cat_split(filename_links))

def loadSteps(filename_steps) :
        global data
	data.list_steps = filemanager.cat_split(filename_steps)


