import random
import data
import time
import os


#
def checkStep(req, lenStep=0) :
	info = req.split('_')
	step = int(info[1])
	width = info[2]
	height = info[3]
	url=req.split('(')[1].split(')')[0]
	steps=stepsOf(url)

	if steps == -1 :
		return "step not found!!!"
	
	sts=steps.split(';')
	if step >= len(sts) :
		return "end of step"
        
        dly = isDelay(steps, step)
        if dly :
                time.sleep(dly)
                req = [ "next", str(step+1), str(width), str(height), "("+url+")"]
                return checkStep("_".join(req), lenStep+1)



        ret=""
        if isText(steps, step) :
            text = steps.split(';')[step]; 
            text = parseSubText(text)
            text = parseSubNumber(text)
            ret = text
        else :
            x, y = scaleStep(steps, step, width, height)
            ret = "x="+str(x)+"&y="+str(y)+'_'+str(isNextText(steps, step))
            
        return "ok_"+ret+"_"+str(lenStep+1)




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


def isNextText(steps, step) :
     if step+1 > len(steps) :
         return False
     return isText(steps, step+1)


def isText(steps, step) :
    s = steps.split(';')[step];
    return s.startswith("text=");
    

def scale(x, y, swidth, sheight, width, height) :
    rx=x * width / swidth
    ry=y * height / sheight
    return rx, ry

def scaleStep(steps, step, width, height) :
        st=steps.split(';')[step];
        sc=steps.split(';')[0];
        xy=st.split('&')
        swh=sc.split('&')
        sx=xy[0].split('=')[1]
        sy=xy[1].split('=')[1]
        swidth=swh[0].split('=')[1]
        sheight=swh[1].split('=')[1]
        return scale(int(sx), int(sy), int(swidth), int(sheight), int(width), int(height))


def parseSubText(text) :
    subtext="${random_text["
    lensub = len(subtext)
    lenText = len(text)
    while True :
        pos = text.find(subtext)
        if pos == -1 :
            break
        otherText = text[:pos]
        pos = pos+lensub
        opos = text.find(']}', pos)
        n=int(text[pos:opos])
        otherText = otherText+randomText(n)
        otherText = otherText+text[opos+2:]
        text = otherText
    return text
    

def parseSubNumber(text) :
    subtext = "${random_number}"
    lensub = len(subtext)
    lenText = len(text)
    while True :
        pos = text.find(subtext)
        if pos == -1 :
            break
        otherText = text[:pos]
        otherText = otherText+str(random.randint(0,9))
        otherText = otherText+text[pos+lensub:]
        text = otherText
    return text


def randomText(count) :
    ret = ""
    for i in range(0, count) :
        ret = ret+str(chr(random.randint(ord('a'), ord('z'))))
    return ret
