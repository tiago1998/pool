import threading
import filemanager, data

def link() :
    global data
    data.current_link += 1
    if not data.current_link < len(data.list_links) :
        data.current_link = 0
    return data.list_links[data.current_link]



def append(req) :
    global data
    
    step = req.split('_')[1].strip('\n').strip('\r')
    l = step[:step.rindex(':')]

    for ar in data.list_links :
        if ar == l :
            return "already have this link"

    data.list_steps.append(step)
    data.list_links.append(l)
    threading.Thread(target=filemanager.save_list, args=(data.filename_links, data.list_links)).start()
    threading.Thread(target=filemanager.save_list, args=(data.filename_steps, data.list_steps)).start()

    return "ok"
