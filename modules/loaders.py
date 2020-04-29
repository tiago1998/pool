
import sys
import filemanager
import data

def loadData() :
    global data

    data.port = sys.argv[1]
    data.filename_links = sys.argv[2]
    data.filename_steps = sys.argv[3]
    data.key = sys.argv[4]


def loadLinks(filename_links) :
        global data
	data.list_links = filemanager.cat_split(filename_links)



def loadSteps(filename_steps) :
        global data
	data.list_steps = filemanager.cat_split(filename_steps)


