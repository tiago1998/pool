import data
import time
import os


#
def checkStep(req, isGetStep=0, lenStep=0) :
	info = req.split('_')
	step = int(info[1])
	display = info[2]
	width = info[3]
	height = info[4]
	url=req.split('(')[1].split(')')[0]
	steps=stepsOf(url)

	if steps == -1 :
		return "step not found!!!"
	
	sts=steps.split(';')
	if step >= len(sts) :
		return "end of step"
        
        dly = isDelay(steps, step)
        if dly :
                print "sleeping "+str(dly)+"sec"
                time.sleep(dly)
                req = [ "next", str(step+1), str(display),
str(width), str(height), "("+url+")"]
                return checkStep("_".join(req), isDoStep, lenStep+1)


        if not isGetStep :
            return doStep(step, steps, display, width, height, url, lenStep+1)
        else :
            st=steps.split(';')[step];
            sc=steps.split(';')[0];
            xy=st.split('&')
            swh=sc.split('&')
            sx=xy[0].split('=')[1]
            sy=xy[1].split('=')[1]
            swidth=swh[0].split('=')[1]
            sheight=swh[1].split('=')[1]
            x,y = scale(int(sx), int(sy), int(swidth), int(sheight), int(width), int(height))
            return "ok_x="+str(x)+"&y="+str(y)+"_"+str(lenStep+1)





#
def doStep(step, steps, display, width, height, url, lenStep) :
        fexec="./utils/doStep.sh"
        if not os.path.isfile(fexec) :
		raise Exception("[!] file "+fexec+" not found.")
	
	ret=os.system(fexec+" '"+str(step)+"' '"+str(steps)+"' '"+str(display)+"' '"+str(width)+"' '"+str(height)+"'")
    	if ret != 0 :
		return "error 512!"

	sts=steps.split(';')
	if step+1 < len(sts) :
                delay=isDelay(steps, step+1)
                if delay :
			time.sleep(delay)
			req = [ "next", str(step+2), str(display), str(width), str(height), "("+url+")"]
			return checkStep("_".join(req), 0, lenStep+1)

	return "ok_"+str(lenStep)






def stepsOf(url) :

    for p in range(len(data.list_steps)) :
        if data.list_steps[p].startswith(url) :
            return data.list_steps[p][len(url)+1:]
    return -1



#
def isDelay(steps, step) :
	s = steps.split(';')[step];

        if s.startswith("delay=") :
		return int(s.split('=')[1])
        return 0

def scale(x, y, swidth, sheight, width, height) :
    rx=x * width / swidth
    ry=y * height / sheight

    return rx, ry
